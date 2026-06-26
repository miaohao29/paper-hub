"""Paper Analysis API Routes"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.analysis_service import AnalysisService

router = APIRouter()
analysis_service = AnalysisService()


@router.post("/{paper_id}/analyze")
async def analyze_paper(
    paper_id: str,
    db: Session = Depends(get_db)
):
    """Analyze a paper to extract innovations and insights"""
    analysis_result = await analysis_service.analyze_paper(db, paper_id)
    if not analysis_result:
        raise HTTPException(status_code=400, detail="Failed to analyze paper")
    return analysis_result


@router.get("/{paper_id}/innovations")
async def get_innovations(
    paper_id: str,
    db: Session = Depends(get_db)
):
    """Get innovation points from a paper"""
    innovations = await analysis_service.get_innovations(db, paper_id)
    return {"paper_id": paper_id, "innovations": innovations}


@router.get("/{paper_id}/relationships")
async def get_paper_relationships(
    paper_id: str,
    db: Session = Depends(get_db)
):
    """Get related papers and relationships"""
    relationships = await analysis_service.get_relationships(db, paper_id)
    return {"paper_id": paper_id, "relationships": relationships}


@router.post("/compare")
async def compare_papers(
    paper_ids: list[str],
    db: Session = Depends(get_db)
):
    """Compare multiple papers"""
    comparison = await analysis_service.compare_papers(db, paper_ids)
    return comparison
