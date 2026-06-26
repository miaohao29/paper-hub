"""Research Trends API Routes"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.analysis_service import AnalysisService

router = APIRouter()
analysis_service = AnalysisService()


@router.get("/")
async def get_trends(
    years: int = 5,
    db: Session = Depends(get_db)
):
    """Get research trends"""
    trends = await analysis_service.analyze_trends(db, years=years)
    return {"trends": trends, "years": years}


@router.get("/topics")
async def get_topic_trends(
    years: int = 5,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Get trending topics"""
    topics = await analysis_service.get_topic_trends(db, years=years, limit=limit)
    return {"topics": topics, "count": len(topics)}


@router.get("/methods")
async def get_methodology_trends(
    years: int = 5,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Get trending methodologies"""
    methods = await analysis_service.get_methodology_trends(db, years=years, limit=limit)
    return {"methods": methods, "count": len(methods)}


@router.get("/timeline")
async def get_timeline(
    db: Session = Depends(get_db)
):
    """Get research timeline"""
    timeline = await analysis_service.get_research_timeline(db)
    return {"timeline": timeline}


@router.get("/emerging")
async def get_emerging_topics(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Get emerging topics"""
    topics = await analysis_service.get_emerging_topics(db, limit=limit)
    return {"emerging_topics": topics, "count": len(topics)}
