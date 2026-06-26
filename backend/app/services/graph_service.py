"""Knowledge Graph Service"""

from sqlalchemy.orm import Session
from typing import Optional, List, Dict
from sqlalchemy import or_

from app.db.models import GraphNode, GraphEdge, Paper, Author


class GraphService:
    """Service for knowledge graph operations"""
    
    async def get_nodes(
        self,
        db: Session,
        node_type: Optional[str] = None
    ) -> List[Dict]:
        """Get all graph nodes"""
        query = db.query(GraphNode)
        if node_type:
            query = query.filter(GraphNode.node_type == node_type)
        
        nodes = query.all()
        return [
            {
                "id": n.id,
                "label": n.label,
                "type": n.node_type,
                "description": n.description
            }
            for n in nodes
        ]
    
    async def get_edges(
        self,
        db: Session,
        source_type: Optional[str] = None,
        target_type: Optional[str] = None
    ) -> List[Dict]:
        """Get all graph edges"""
        query = db.query(GraphEdge).join(
            GraphNode,
            GraphEdge.source_node_id == GraphNode.id
        )
        
        if source_type:
            query = query.filter(GraphNode.node_type == source_type)
        
        edges = query.all()
        return [
            {
                "source": e.source_node_id,
                "target": e.target_node_id,
                "type": e.edge_type,
                "weight": e.weight
            }
            for e in edges
        ]
    
    async def search(
        self,
        db: Session,
        query: str,
        limit: int = 10
    ) -> List[Dict]:
        """Search knowledge graph"""
        nodes = db.query(GraphNode).filter(
            or_(
                GraphNode.label.ilike(f"%{query}%"),
                GraphNode.description.ilike(f"%{query}%")
            )
        ).limit(limit).all()
        
        return [
            {
                "id": n.id,
                "label": n.label,
                "type": n.node_type,
                "description": n.description
            }
            for n in nodes
        ]
    
    async def get_communities(
        self,
        db: Session
    ) -> List[Dict]:
        """Get graph communities using graph algorithms"""
        # Placeholder - would implement community detection
        return []
    
    async def get_insights(
        self,
        db: Session
    ) -> Dict:
        """Get graph insights"""
        # Count nodes and edges
        node_count = db.query(GraphNode).count()
        edge_count = db.query(GraphEdge).count()
        
        # Get node types distribution
        node_types = db.query(
            GraphNode.node_type,
            func.count(GraphNode.id).label('count')
        ).group_by(GraphNode.node_type).all()
        
        return {
            "total_nodes": node_count,
            "total_edges": edge_count,
            "node_types": [
                {"type": nt[0], "count": nt[1]}
                for nt in node_types
            ]
        }
    
    async def get_neighbors(
        self,
        db: Session,
        node_id: str,
        hops: int = 1
    ) -> List[Dict]:
        """Get neighbors of a node"""
        neighbors = []
        
        # Get direct neighbors
        edges = db.query(GraphEdge).filter(
            or_(
                GraphEdge.source_node_id == node_id,
                GraphEdge.target_node_id == node_id
            )
        ).all()
        
        for edge in edges:
            neighbor_id = (
                edge.target_node_id if edge.source_node_id == node_id
                else edge.source_node_id
            )
            neighbor = db.query(GraphNode).filter(
                GraphNode.id == neighbor_id
            ).first()
            
            if neighbor:
                neighbors.append({
                    "id": neighbor.id,
                    "label": neighbor.label,
                    "type": neighbor.node_type,
                    "edge_type": edge.edge_type
                })
        
        return neighbors


# Import after class definition
from sqlalchemy import func
