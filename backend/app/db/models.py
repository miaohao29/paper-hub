"""SQLAlchemy Database Models"""

from sqlalchemy import Column, String, Text, Integer, Float, DateTime, ForeignKey, Table, JSON, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base
from app.db.base import BaseMixin


# Association table for paper-author relationship
paper_author_association = Table(
    'paper_author_association',
    Base.metadata,
    Column('paper_id', String(36), ForeignKey('papers.id')),
    Column('author_id', String(36), ForeignKey('authors.id'))
)


# Association table for paper-keyword relationship
paper_keyword_association = Table(
    'paper_keyword_association',
    Base.metadata,
    Column('paper_id', String(36), ForeignKey('papers.id')),
    Column('keyword_id', String(36), ForeignKey('keywords.id'))
)


class Paper(BaseMixin, Base):
    """Paper Model"""
    __tablename__ = "papers"
    
    title = Column(String(500), nullable=False, index=True)
    abstract = Column(Text)
    content = Column(Text)  # Full text extracted from PDF/DOCX
    doi = Column(String(100), unique=True, index=True)
    arxiv_id = Column(String(100), unique=True, index=True)
    publication_year = Column(Integer)
    publication_date = Column(DateTime)
    venue = Column(String(200))  # Journal/Conference name
    file_path = Column(String(500))
    file_type = Column(String(20))  # pdf, docx, txt, md
    
    # Relations
    authors = relationship('Author', secondary=paper_author_association, back_populates='papers')
    keywords = relationship('Keyword', secondary=paper_keyword_association, back_populates='papers')
    analyses = relationship('Analysis', back_populates='paper', cascade='all, delete-orphan')
    innovations = relationship('Innovation', back_populates='paper', cascade='all, delete-orphan')
    
    # Metadata
    citation_count = Column(Integer, default=0)
    view_count = Column(Integer, default=0)
    embedding_vector = Column(JSON)  # For vector search
    processed = Column(Boolean, default=False)
    error_message = Column(Text)


class Author(BaseMixin, Base):
    """Author Model"""
    __tablename__ = "authors"
    
    name = Column(String(200), nullable=False, index=True)
    email = Column(String(100))
    affiliation = Column(String(300))
    orcid = Column(String(100))
    
    # Relations
    papers = relationship('Paper', secondary=paper_author_association, back_populates='authors')


class Keyword(BaseMixin, Base):
    """Keyword Model"""
    __tablename__ = "keywords"
    
    keyword = Column(String(100), nullable=False, unique=True, index=True)
    category = Column(String(50))  # Topic, Method, Tool, etc.
    frequency = Column(Integer, default=1)
    
    # Relations
    papers = relationship('Paper', secondary=paper_keyword_association, back_populates='keywords')


class Analysis(BaseMixin, Base):
    """Paper Analysis Results"""
    __tablename__ = "analyses"
    
    paper_id = Column(String(36), ForeignKey('papers.id'), nullable=False)
    analysis_type = Column(String(50))  # innovation, summary, comparison, etc.
    result = Column(JSON, nullable=False)
    confidence_score = Column(Float)
    
    # Relations
    paper = relationship('Paper', back_populates='analyses')


class Innovation(BaseMixin, Base):
    """Innovation Points in Papers"""
    __tablename__ = "innovations"
    
    paper_id = Column(String(36), ForeignKey('papers.id'), nullable=False)
    title = Column(String(300), nullable=False)
    description = Column(Text, nullable=False)
    innovation_type = Column(String(50))  # Method, Tool, Theory, Application
    significance_score = Column(Float)  # 0-1
    related_innovations = Column(JSON)  # List of related innovation IDs
    
    # Relations
    paper = relationship('Paper', back_populates='innovations')


class GraphNode(BaseMixin, Base):
    """Knowledge Graph Node"""
    __tablename__ = "graph_nodes"
    
    label = Column(String(300), nullable=False, index=True)
    node_type = Column(String(50), nullable=False)  # paper, author, concept, methodology
    description = Column(Text)
    entity_id = Column(String(100), index=True)  # Reference to paper_id, author_id, etc.
    metadata = Column(JSON)
    embedding_vector = Column(JSON)


class GraphEdge(BaseMixin, Base):
    """Knowledge Graph Edge"""
    __tablename__ = "graph_edges"
    
    source_node_id = Column(String(36), ForeignKey('graph_nodes.id'), nullable=False)
    target_node_id = Column(String(36), ForeignKey('graph_nodes.id'), nullable=False)
    edge_type = Column(String(50), nullable=False)  # cites, similar, uses, etc.
    weight = Column(Float, default=1.0)
    metadata = Column(JSON)


class Trend(BaseMixin, Base):
    """Research Trend Analysis"""
    __tablename__ = "trends"
    
    trend_name = Column(String(300), nullable=False, index=True)
    trend_type = Column(String(50))  # topic, methodology, tool
    start_year = Column(Integer)
    end_year = Column(Integer)
    growth_rate = Column(Float)
    paper_count = Column(Integer)
    description = Column(Text)
    metadata = Column(JSON)
