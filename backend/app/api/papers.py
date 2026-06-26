"""Paper Management API Routes"""

from fastapi import APIRouter, HTTPException, File, UploadFile, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.schemas import (
    PaperCreate, PaperResponse, PaperUpdate, PaperListResponse
)
from app.services.paper_service import PaperService

router = APIRouter()
paper_service = PaperService()


@router.get("/", response_model=PaperListResponse)
async def list_papers(
    skip: int = 0,
    limit: int = 20,
    search: str = None,
    db: Session = Depends(get_db)
):
    """List all papers with pagination and search"""
    papers, total = await paper_service.list_papers(db, skip=skip, limit=limit, search=search)
    return PaperListResponse(
        papers=papers,
        total=total,
        skip=skip,
        limit=limit
    )


@router.post("/", response_model=PaperResponse)
async def create_paper(
    paper: PaperCreate,
    db: Session = Depends(get_db)
):
    """Create a new paper"""
    return await paper_service.create_paper(db, paper)


@router.post("/upload", response_model=PaperResponse)
async def upload_paper(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload a paper file (PDF or DOCX)"""
    return await paper_service.upload_paper(db, file)


@router.get("/{paper_id}", response_model=PaperResponse)
async def get_paper(
    paper_id: str,
    db: Session = Depends(get_db)
):
    """Get a specific paper by ID"""
    paper = await paper_service.get_paper(db, paper_id)
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")
    return paper


@router.put("/{paper_id}", response_model=PaperResponse)
async def update_paper(
    paper_id: str,
    paper_update: PaperUpdate,
    db: Session = Depends(get_db)
):
    """Update a paper"""
    paper = await paper_service.update_paper(db, paper_id, paper_update)
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")
    return paper


@router.delete("/{paper_id}")
async def delete_paper(
    paper_id: str,
    db: Session = Depends(get_db)
):
    """Delete a paper"""
    success = await paper_service.delete_paper(db, paper_id)
    if not success:
        raise HTTPException(status_code=404, detail="Paper not found")
    return {"message": "Paper deleted successfully"}


@router.post("/arxiv/import")
async def import_from_arxiv(
    arxiv_id: str,
    db: Session = Depends(get_db)
):
    """Import a paper from arXiv"""
    paper = await paper_service.import_from_arxiv(db, arxiv_id)
    if not paper:
        raise HTTPException(status_code=400, detail="Failed to import from arXiv")
    return paper
