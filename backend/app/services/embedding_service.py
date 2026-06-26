"""Embedding and Vector Database Service"""

from typing import List, Optional
from app.config import get_settings

settings = get_settings()


class EmbeddingService:
    """Service for generating embeddings and vector search"""
    
    def __init__(self):
        self.provider = settings.embedding_provider
        self.model = settings.embedding_model
        
        if self.provider == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=settings.embedding_api_key)
        
        # Initialize LanceDB
        import lancedb
        self.db = lancedb.connect(settings.lancedb_path)
    
    async def embed_text(self, text: str) -> List[float]:
        """Generate embedding for text"""
        if self.provider == "openai":
            response = self.client.embeddings.create(
                model=self.model,
                input=text
            )
            return response.data[0].embedding
        
        return []
    
    async def embed_texts(
        self,
        texts: List[str],
        batch_size: int = 100
    ) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        embeddings = []
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            
            if self.provider == "openai":
                response = self.client.embeddings.create(
                    model=self.model,
                    input=batch
                )
                embeddings.extend([e.embedding for e in response.data])
        
        return embeddings
    
    async def search(
        self,
        query_embedding: List[float],
        table_name: str = "papers",
        limit: int = 10
    ) -> List[dict]:
        """Search vector database"""
        try:
            table = self.db.open_table(table_name)
            results = table.search(query_embedding).limit(limit).to_list()
            return results
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    async def add_embeddings(
        self,
        documents: List[dict],
        table_name: str = "papers"
    ) -> bool:
        """Add embeddings to vector database"""
        try:
            table = self.db.create_table(table_name, data=documents, mode="overwrite")
            return True
        except Exception as e:
            print(f"Add embeddings error: {e}")
            return False
