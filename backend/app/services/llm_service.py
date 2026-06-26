"""LLM Integration Service"""

from typing import Optional, List
from app.config import get_settings

settings = get_settings()


class LLMService:
    """Service for LLM operations"""
    
    def __init__(self):
        self.provider = settings.llm_provider
        self.model = settings.llm_model
        self.temperature = settings.llm_temperature
        self.max_tokens = settings.llm_max_tokens
        
        if self.provider == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=settings.llm_api_key)
        elif self.provider == "anthropic":
            import anthropic
            self.client = anthropic.Anthropic(api_key=settings.llm_api_key)
    
    async def extract_innovations(self, content: str) -> List[str]:
        """Extract innovations from paper content"""
        prompt = f"""
Please identify and extract the main innovations from the following paper content.
Return a JSON list of innovations with title and description.

Content:
{content[:3000]}

Return format: [{{'title': '...', 'description': '...', 'type': '...', 'significance': 0-1}}]
"""
        
        response = await self._call_llm(prompt)
        return response
    
    async def summarize_paper(self, content: str) -> str:
        """Summarize paper content"""
        prompt = f"""
Please provide a concise summary of the following paper:

{content[:3000]}

Summary should be 2-3 sentences and highlight the main contributions.
"""
        
        return await self._call_llm(prompt)
    
    async def analyze_relationships(self, papers_content: List[str]) -> dict:
        """Analyze relationships between papers"""
        content = "\n\n".join(papers_content[:3])
        
        prompt = f"""
Please analyze the relationships between these papers:

{content}

Identify: common themes, methodologies, authors, and how they build on each other.
"""
        
        return await self._call_llm(prompt)
    
    async def _call_llm(self, prompt: str) -> str:
        """Call LLM API"""
        if self.provider == "openai":
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a research paper analysis assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content
        
        elif self.provider == "anthropic":
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        
        elif self.provider == "local":
            import requests
            response = requests.post(
                f"{settings.llm_base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            return response.json()["response"]
        
        return ""
