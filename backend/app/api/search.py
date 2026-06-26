"""Search API Routes"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.search_service import SearchService

router = APIRouter()
search_service = SearchService()


@router.post("/")
async def semantic_search(
    query: str,
    limit: int = 20,
    filters: dict = None,
    db: Session = Depends(get_db)
):
    """Semantic search across papers and knowledge base"""
    results = await search_service.semantic_search(db, query, limit=limit, filters=filters)
    return {
        "query": query,
        "results": results,
        "count": len(results)
    }


@router.post("/citations")
async def citation_search(
    paper_id: str,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Search papers cited by or citing a given paper"""
    citations = await search_service.citation_search(db, paper_id, limit=limit)
    return {
        "paper_id": paper_id,
        "citations": citations,
        "count": len(citations)
    }


@router.post("/authors")
async def author_search(
    author_name: str,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Search papers by author"""
    papers = await search_service.author_search(db, author_name, limit=limit)
    return {
        "author": author_name,
        "papers": papers,
        "count": len(papers)
    }


@router.post("/advanced")
async def advanced_search(
    query: str,
    filters: dict,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Advanced search with multiple filters"""
    results = await search_service.advanced_search(db, query, filters=filters, limit=limit)
    return {
        "query": query,
        "filters": filters,
        "results": results,
        "count": len(results)
    }
