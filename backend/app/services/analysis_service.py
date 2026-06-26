"""Paper Analysis Service"""

from sqlalchemy.orm import Session
from typing import Optional, List, Dict
from app.db.models import Paper, Analysis, Innovation
from app.services.llm_service import LLMService

llm_service = LLMService()


class AnalysisService:
    """Service for analyzing papers"""
    
    async def analyze_paper(
        self,
        db: Session,
        paper_id: str
    ) -> Optional[Dict]:
        """Analyze a paper to extract innovations and insights"""
        paper = db.query(Paper).filter(Paper.id == paper_id).first()
        if not paper:
            return None
        
        # Extract innovations
        innovations = await self._extract_innovations(db, paper)
        
        # Get relationships
        relationships = await self._get_relationships(db, paper)
        
        # Create analysis record
        analysis_result = {
            "paper_id": paper_id,
            "title": paper.title,
            "innovations": innovations,
            "relationships": relationships,
            "summary": await self._summarize_paper(db, paper)
        }
        
        analysis = Analysis(
            paper_id=paper_id,
            analysis_type="comprehensive",
            result=analysis_result
        )
        db.add(analysis)
        db.commit()
        
        return analysis_result
    
    async def get_innovations(
        self,
        db: Session,
        paper_id: str
    ) -> List[Dict]:
        """Get innovation points from a paper"""
        innovations = db.query(Innovation).filter(
            Innovation.paper_id == paper_id
        ).all()
        
        return [
            {
                "id": inn.id,
                "title": inn.title,
                "description": inn.description,
                "type": inn.innovation_type,
                "significance": inn.significance_score
            }
            for inn in innovations
        ]
    
    async def get_relationships(
        self,
        db: Session,
        paper_id: str
    ) -> List[Dict]:
        """Get related papers and relationships"""
        # This would use the knowledge graph
        # For now, return related papers by keywords
        paper = db.query(Paper).filter(Paper.id == paper_id).first()
        if not paper:
            return []
        
        related_papers = []
        for keyword in paper.keywords:
            papers = db.query(Paper).filter(
                Paper.keywords.any(Keyword.id == keyword.id),
                Paper.id != paper_id
            ).limit(5).all()
            related_papers.extend(papers)
        
        # Remove duplicates
        seen = set()
        unique_papers = []
        for p in related_papers:
            if p.id not in seen:
                seen.add(p.id)
                unique_papers.append({
                    "id": p.id,
                    "title": p.title,
                    "venue": p.venue,
                    "year": p.publication_year
                })
        
        return unique_papers
    
    async def compare_papers(
        self,
        db: Session,
        paper_ids: List[str]
    ) -> Dict:
        """Compare multiple papers"""
        papers = []
        for pid in paper_ids:
            paper = db.query(Paper).filter(Paper.id == pid).first()
            if paper:
                papers.append(paper)
        
        if not papers:
            return {}
        
        comparison = {
            "papers": [
                {
                    "id": p.id,
                    "title": p.title,
                    "authors": [a.name for a in p.authors],
                    "year": p.publication_year,
                    "keywords": [k.keyword for k in p.keywords]
                }
                for p in papers
            ],
            "common_keywords": await self._get_common_keywords(papers),
            "time_range": {
                "min": min(p.publication_year for p in papers if p.publication_year),
                "max": max(p.publication_year for p in papers if p.publication_year)
            }
        }
        
        return comparison
    
    async def analyze_trends(
        self,
        db: Session,
        years: int = 5
    ) -> Dict:
        """Analyze research trends"""
        # Get papers from last N years
        from datetime import datetime, timedelta
        cutoff_year = datetime.now().year - years
        
        papers = db.query(Paper).filter(
            Paper.publication_year >= cutoff_year
        ).all()
        
        # Group by year and keywords
        trends_by_year = {}
        for paper in papers:
            year = paper.publication_year
            if year not in trends_by_year:
                trends_by_year[year] = {}
            
            for keyword in paper.keywords:
                if keyword.keyword not in trends_by_year[year]:
                    trends_by_year[year][keyword.keyword] = 0
                trends_by_year[year][keyword.keyword] += 1
        
        return trends_by_year
    
    async def get_topic_trends(
        self,
        db: Session,
        years: int = 5,
        limit: int = 10
    ) -> List[Dict]:
        """Get trending topics"""
        # Group keywords by frequency
        from sqlalchemy import desc
        
        trends = db.query(
            Keyword.keyword,
            func.count(Paper.id).label('count')
        ).join(Paper).filter(
            Paper.publication_year >= datetime.now().year - years
        ).group_by(Keyword.keyword).order_by(desc('count')).limit(limit).all()
        
        return [
            {"topic": t[0], "frequency": t[1]}
            for t in trends
        ]
    
    async def get_methodology_trends(
        self,
        db: Session,
        years: int = 5,
        limit: int = 10
    ) -> List[Dict]:
        """Get trending methodologies"""
        # Similar to topic trends, filter by methodology keywords
        from sqlalchemy import desc
        
        trends = db.query(
            Keyword.keyword,
            func.count(Paper.id).label('count')
        ).join(Paper).filter(
            Paper.publication_year >= datetime.now().year - years,
            Keyword.category == 'methodology'
        ).group_by(Keyword.keyword).order_by(desc('count')).limit(limit).all()
        
        return [
            {"methodology": t[0], "frequency": t[1]}
            for t in trends
        ]
    
    async def get_research_timeline(self, db: Session) -> Dict:
        """Get research timeline"""
        from sqlalchemy import func
        
        timeline = db.query(
            Paper.publication_year,
            func.count(Paper.id).label('count')
        ).group_by(Paper.publication_year).order_by(Paper.publication_year).all()
        
        return {
            "timeline": [
                {"year": t[0], "count": t[1]}
                for t in timeline
            ]
        }
    
    async def get_emerging_topics(
        self,
        db: Session,
        limit: int = 10
    ) -> List[str]:
        """Get emerging topics (recent keywords)"""
        from sqlalchemy import desc
        from datetime import datetime, timedelta
        
        recent_date = datetime.now() - timedelta(days=180)
        
        topics = db.query(
            Keyword.keyword,
            func.count(Paper.id).label('count')
        ).join(Paper).filter(
            Paper.created_at >= recent_date
        ).group_by(Keyword.keyword).order_by(
            desc('count')
        ).limit(limit).all()
        
        return [t[0] for t in topics]
    
    async def _extract_innovations(
        self,
        db: Session,
        paper: Paper
    ) -> List[Dict]:
        """Extract innovation points using LLM"""
        if not paper.content:
            return []
        
        innovations_text = await llm_service.extract_innovations(paper.content)
        # Parse and store innovations
        return innovations_text
    
    async def _get_relationships(
        self,
        db: Session,
        paper: Paper
    ) -> List[Dict]:
        """Get paper relationships"""
        return []
    
    async def _summarize_paper(
        self,
        db: Session,
        paper: Paper
    ) -> str:
        """Summarize paper using LLM"""
        if not paper.content:
            return paper.abstract or ""
        
        return await llm_service.summarize_paper(paper.content)
    
    async def _get_common_keywords(
        self,
        papers: List[Paper]
    ) -> List[str]:
        """Get common keywords across papers"""
        if not papers:
            return []
        
        keyword_sets = [
            set(k.keyword for k in p.keywords)
            for p in papers
        ]
        
        common = keyword_sets[0]
        for kset in keyword_sets[1:]:
            common = common.intersection(kset)
        
        return list(common)


# Import after class definition to avoid circular imports
from sqlalchemy import func
from app.db.models import Keyword
from datetime import datetime
