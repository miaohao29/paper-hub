"""Application Configuration"""

from typing import List, Optional
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application Settings"""
    
    # Database
    database_url: str = "postgresql://user:password@localhost:5432/paper_hub"
    database_pool_size: int = 20
    
    # Redis
    redis_url: str = "redis://localhost:6379/0"
    
    # LLM Configuration
    llm_provider: str = "openai"  # openai, anthropic, local
    llm_api_key: Optional[str] = None
    llm_model: str = "gpt-4"
    llm_temperature: float = 0.3
    llm_max_tokens: int = 2000
    llm_timeout: int = 60
    llm_base_url: Optional[str] = None  # For local LLMs
    
    # Embedding Configuration
    embedding_provider: str = "openai"
    embedding_api_key: Optional[str] = None
    embedding_model: str = "text-embedding-3-small"
    embedding_batch_size: int = 100
    embedding_dimension: int = 1536  # For text-embedding-3-small
    
    # Vector Database
    lancedb_path: str = "./lancedb"
    
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    cors_origins: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    # File Upload
    upload_dir: str = "./uploads"
    max_file_size: int = 104857600  # 100MB
    allowed_extensions: List[str] = ["pdf", "docx", "txt", "md"]
    
    # arXiv
    arxiv_enabled: bool = True
    arxiv_rate_limit: int = 5
    
    # Logging
    log_level: str = "INFO"
    
    # Frontend
    frontend_url: str = "http://localhost:5173"
    
    # Celery
    celery_broker_url: str = "redis://localhost:6379/0"
    celery_result_backend: str = "redis://localhost:6379/0"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get application settings (cached)"""
    return Settings()
