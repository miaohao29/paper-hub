"""Pydantic Schemas for Request/Response Validation"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# Author Schemas
class AuthorBase(BaseModel):
    name: str
    email: Optional[str] = None
    affiliation: Optional[str] = None
    orcid: Optional[str] = None


class AuthorCreate(AuthorBase):
    pass


class AuthorResponse(AuthorBase):
    id: str
    created_at: datetime
    
    class Config:
        from_attributes = True


# Keyword Schemas
class KeywordBase(BaseModel):
    keyword: str
    category: Optional[str] = None


class KeywordResponse(KeywordBase):
    id: str
    frequency: int
    
    class Config:
        from_attributes = True


# Paper Schemas
class PaperBase(BaseModel):
    title: str
    abstract: Optional[str] = None
    doi: Optional[str] = None
    arxiv_id: Optional[str] = None
    publication_year: Optional[int] = None
    publication_date: Optional[datetime] = None
    venue: Optional[str] = None


class PaperCreate(PaperBase):
    authors: Optional[List[AuthorCreate]] = []
    keywords: Optional[List[str]] = []


class PaperUpdate(BaseModel):
    title: Optional[str] = None
    abstract: Optional[str] = None
    venue: Optional[str] = None


class PaperResponse(PaperBase):
    id: str
    content: Optional[str] = None
    file_path: Optional[str] = None
    file_type: Optional[str] = None
    authors: List[AuthorResponse] = []
    keywords: List[KeywordResponse] = []
    citation_count: int = 0
    view_count: int = 0
    processed: bool = False
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class PaperListResponse(BaseModel):
    papers: List[PaperResponse]
    total: int
    skip: int
    limit: int


# Innovation Schemas
class InnovationBase(BaseModel):
    title: str
    description: str
    innovation_type: str
    significance_score: Optional[float] = None


class InnovationResponse(InnovationBase):
    id: str
    paper_id: str
    created_at: datetime
    
    class Config:
        from_attributes = True


# Analysis Schemas
class AnalysisBase(BaseModel):
    analysis_type: str
    result: dict
    confidence_score: Optional[float] = None


class AnalysisResponse(AnalysisBase):
    id: str
    paper_id: str
    created_at: datetime
    
    class Config:
        from_attributes = True


# Graph Schemas
class GraphNodeBase(BaseModel):
    label: str
    node_type: str
    description: Optional[str] = None
    entity_id: Optional[str] = None


class GraphNodeResponse(GraphNodeBase):
    id: str
    metadata: Optional[dict] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class GraphEdgeBase(BaseModel):
    source_node_id: str
    target_node_id: str
    edge_type: str
    weight: Optional[float] = 1.0


class GraphEdgeResponse(GraphEdgeBase):
    id: str
    created_at: datetime
    
    class Config:
        from_attributes = True


# Trend Schemas
class TrendBase(BaseModel):
    trend_name: str
    trend_type: str
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    growth_rate: Optional[float] = None
    paper_count: Optional[int] = None


class TrendResponse(TrendBase):
    id: str
    description: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True
