"""Semantic Search Service"""

from sqlalchemy.orm import Session
from typing import Optional, List, Dict
from sqlalchemy import or_, func

from app.db.models import Paper, Author, Keyword
from app.services.embedding_service import EmbeddingService

embedding_service = EmbeddingService()


class SearchService:
    """Service for searching papers and knowledge base"""
    
    async def semantic_search(
        self,
        db: Session,
        query: str,
        limit: int = 20,
        filters: Optional[Dict] = None
    ) -> List[Dict]:
        """Semantic search across papers"""
        # Get embedding for query
        query_embedding = await embedding_service.embed_text(query)
        
        # Search in database (placeholder - would use vector DB)
        papers = db.query(Paper).filter(
            or_(
                Paper.title.ilike(f"%{query}%"),
                Paper.abstract.ilike(f"%{query}%"),
                Paper.keywords.any(Keyword.keyword.ilike(f"%{query}%"))
            )
        ).limit(limit).all()
        
        results = [
            {
                "id": p.id,
                "title": p.title,
                "abstract": p.abstract[:200] if p.abstract else None,
                "authors": [a.name for a in p.authors],
                "year": p.publication_year,
                "relevance_score": 0.85  # Placeholder
            }
            for p in papers
        ]
        
        return results
    
    async def citation_search(
        self,
        db: Session,
        paper_id: str,
        limit: int = 20
    ) -> List[Dict]:
        """Search papers cited by or citing a paper"""
        # This would use the knowledge graph
        paper = db.query(Paper).filter(Paper.id == paper_id).first()
        if not paper:
            return []
        
        # Find papers with similar keywords
        related = db.query(Paper).filter(
            Paper.keywords.any(Keyword.id.in_(
                [k.id for k in paper.keywords]
            )),
            Paper.id != paper_id
        ).limit(limit).all()
        
        return [
            {
                "id": p.id,
                "title": p.title,
                "authors": [a.name for a in p.authors],
                "year": p.publication_year
            }
            for p in related
        ]
    
    async def author_search(
        self,
        db: Session,
        author_name: str,
        limit: int = 20
    ) -> List[Dict]:
        """Search papers by author"""
        authors = db.query(Author).filter(
            Author.name.ilike(f"%{author_name}%")
        ).all()
        
        papers = []
        for author in authors:
            papers.extend(author.papers)
        
        return [
            {
                "id": p.id,
                "title": p.title,
                "year": p.publication_year,
                "authors": [a.name for a in p.authors]
            }
            for p in papers[:limit]
        ]
    
    async def advanced_search(
        self,
        db: Session,
        query: str,
        filters: Optional[Dict] = None,
        limit: int = 20
    ) -> List[Dict]:
        """Advanced search with multiple filters"""
        q = db.query(Paper)
        
        # Apply text search
        q = q.filter(
            or_(
                Paper.title.ilike(f"%{query}%"),
                Paper.abstract.ilike(f"%{query}%")
            )
        )
        
        # Apply filters
        if filters:
            if "year_from" in filters:
                q = q.filter(Paper.publication_year >= filters["year_from"])
            if "year_to" in filters:
                q = q.filter(Paper.publication_year <= filters["year_to"])
            if "authors" in filters:
                q = q.filter(Paper.authors.any(
                    Author.name.in_(filters["authors"])
                ))
            if "keywords" in filters:
                q = q.filter(Paper.keywords.any(
                    Keyword.keyword.in_(filters["keywords"])
                ))
        
        papers = q.limit(limit).all()
        
        return [
            {
                "id": p.id,
                "title": p.title,
                "abstract": p.abstract[:200] if p.abstract else None,
                "authors": [a.name for a in p.authors],
                "year": p.publication_year,
                "keywords": [k.keyword for k in p.keywords]
            }
            for p in papers
        ]
