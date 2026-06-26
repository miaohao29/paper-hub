"""Paper Management Service"""

from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from typing import Optional, Tuple, List
import os
from datetime import datetime

from app.db.models import Paper, Author, Keyword
from app.models.schemas import PaperCreate, PaperUpdate, PaperResponse
from app.config import get_settings
from app.utils.validators import validate_file

settings = get_settings()


class PaperService:
    """Service for managing papers"""
    
    async def list_papers(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 20,
        search: Optional[str] = None
    ) -> Tuple[List[Paper], int]:
        """List all papers with optional search"""
        query = db.query(Paper)
        
        if search:
            query = query.filter(
                or_(
                    Paper.title.ilike(f"%{search}%"),
                    Paper.abstract.ilike(f"%{search}%"),
                    Paper.doi.ilike(f"%{search}%")
                )
            )
        
        total = query.count()
        papers = query.offset(skip).limit(limit).all()
        return papers, total
    
    async def get_paper(self, db: Session, paper_id: str) -> Optional[Paper]:
        """Get a specific paper"""
        paper = db.query(Paper).filter(Paper.id == paper_id).first()
        if paper:
            paper.view_count += 1
            db.commit()
        return paper
    
    async def create_paper(
        self,
        db: Session,
        paper_data: PaperCreate
    ) -> Paper:
        """Create a new paper"""
        paper = Paper(
            title=paper_data.title,
            abstract=paper_data.abstract,
            doi=paper_data.doi,
            arxiv_id=paper_data.arxiv_id,
            publication_year=paper_data.publication_year,
            publication_date=paper_data.publication_date,
            venue=paper_data.venue
        )
        
        # Add authors
        if paper_data.authors:
            for author_data in paper_data.authors:
                author = db.query(Author).filter(
                    Author.name == author_data.name
                ).first()
                if not author:
                    author = Author(**author_data.dict())
                    db.add(author)
                paper.authors.append(author)
        
        # Add keywords
        if paper_data.keywords:
            for keyword_text in paper_data.keywords:
                keyword = db.query(Keyword).filter(
                    Keyword.keyword == keyword_text
                ).first()
                if not keyword:
                    keyword = Keyword(keyword=keyword_text)
                    db.add(keyword)
                else:
                    keyword.frequency += 1
                paper.keywords.append(keyword)
        
        db.add(paper)
        db.commit()
        db.refresh(paper)
        return paper
    
    async def update_paper(
        self,
        db: Session,
        paper_id: str,
        paper_update: PaperUpdate
    ) -> Optional[Paper]:
        """Update a paper"""
        paper = db.query(Paper).filter(Paper.id == paper_id).first()
        if not paper:
            return None
        
        update_data = paper_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(paper, field, value)
        
        db.commit()
        db.refresh(paper)
        return paper
    
    async def delete_paper(
        self,
        db: Session,
        paper_id: str
    ) -> bool:
        """Delete a paper"""
        paper = db.query(Paper).filter(Paper.id == paper_id).first()
        if not paper:
            return False
        
        # Delete associated file
        if paper.file_path and os.path.exists(paper.file_path):
            os.remove(paper.file_path)
        
        db.delete(paper)
        db.commit()
        return True
    
    async def upload_paper(
        self,
        db: Session,
        file
    ) -> Paper:
        """Upload a paper file"""
        # Validate file
        if not validate_file(file.filename):
            raise ValueError("Invalid file type")
        
        # Save file
        os.makedirs(settings.upload_dir, exist_ok=True)
        file_path = os.path.join(settings.upload_dir, file.filename)
        
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Create paper record
        paper = Paper(
            title=file.filename.split('.')[0],
            file_path=file_path,
            file_type=file.filename.split('.')[-1]
        )
        
        db.add(paper)
        db.commit()
        db.refresh(paper)
        return paper
    
    async def import_from_arxiv(
        self,
        db: Session,
        arxiv_id: str
    ) -> Optional[Paper]:
        """Import a paper from arXiv"""
        from app.utils.arxiv_fetcher import fetch_arxiv_paper
        
        paper_data = await fetch_arxiv_paper(arxiv_id)
        if not paper_data:
            return None
        
        # Check if already exists
        existing = db.query(Paper).filter(
            Paper.arxiv_id == arxiv_id
        ).first()
        if existing:
            return existing
        
        return await self.create_paper(db, paper_data)
