"""arXiv API Integration"""

import feedparser
from app.models.schemas import PaperCreate, AuthorCreate
from datetime import datetime


async def fetch_arxiv_paper(arxiv_id: str) -> dict:
    """Fetch paper from arXiv"""
    try:
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
        response = feedparser.parse(url)
        
        if not response.entries:
            return None
        
        entry = response.entries[0]
        
        # Extract authors
        authors = [
            AuthorCreate(name=author.name)
            for author in entry.get('authors', [])
        ]
        
        # Extract publication date
        pub_date = datetime.fromisoformat(
            entry.get('published', '')[:10]
        ) if entry.get('published') else None
        
        paper_data = PaperCreate(
            title=entry.title,
            abstract=entry.summary,
            arxiv_id=arxiv_id,
            publication_date=pub_date,
            authors=authors,
            keywords=[tag.term for tag in entry.get('tags', [])]
        )
        
        return paper_data
    
    except Exception as e:
        print(f"arXiv fetch error: {e}")
        return None
