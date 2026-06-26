"""Knowledge Graph API Routes"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.graph_service import GraphService

router = APIRouter()
graph_service = GraphService()


@router.get("/nodes")
async def get_graph_nodes(
    node_type: str = None,
    db: Session = Depends(get_db)
):
    """Get all knowledge graph nodes"""
    nodes = await graph_service.get_nodes(db, node_type=node_type)
    return {"nodes": nodes, "count": len(nodes)}


@router.get("/edges")
async def get_graph_edges(
    source_type: str = None,
    target_type: str = None,
    db: Session = Depends(get_db)
):
    """Get all knowledge graph edges"""
    edges = await graph_service.get_edges(db, source_type=source_type, target_type=target_type)
    return {"edges": edges, "count": len(edges)}


@router.post("/search")
async def search_graph(
    query: str,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Search knowledge graph"""
    results = await graph_service.search(db, query, limit=limit)
    return {"results": results, "count": len(results)}


@router.get("/communities")
async def get_communities(
    db: Session = Depends(get_db)
):
    """Get graph communities"""
    communities = await graph_service.get_communities(db)
    return {"communities": communities, "count": len(communities)}


@router.get("/insights")
async def get_graph_insights(
    db: Session = Depends(get_db)
):
    """Get graph insights"""
    insights = await graph_service.get_insights(db)
    return insights


@router.get("/neighbors/{node_id}")
async def get_node_neighbors(
    node_id: str,
    hops: int = 1,
    db: Session = Depends(get_db)
):
    """Get neighbors of a node"""
    neighbors = await graph_service.get_neighbors(db, node_id, hops=hops)
    return {"node_id": node_id, "neighbors": neighbors}
