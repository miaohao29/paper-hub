"""Document Extraction Service"""

from typing import Optional
import os


class ExtractionService:
    """Service for extracting text from documents"""
    
    async def extract_from_pdf(self, file_path: str) -> Optional[str]:
        """Extract text from PDF"""
        try:
            from PyPDF2 import PdfReader
            
            text = ""
            with open(file_path, 'rb') as f:
                pdf_reader = PdfReader(f)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            print(f"PDF extraction error: {e}")
            return None
    
    async def extract_from_docx(self, file_path: str) -> Optional[str]:
        """Extract text from DOCX"""
        try:
            from docx import Document
            
            doc = Document(file_path)
            text = ""
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        except Exception as e:
            print(f"DOCX extraction error: {e}")
            return None
    
    async def extract_from_txt(self, file_path: str) -> Optional[str]:
        """Extract text from TXT"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"TXT extraction error: {e}")
            return None
    
    async def extract_text(
        self,
        file_path: str
    ) -> Optional[str]:
        """Extract text from any supported format"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower().lstrip('.')
        
        if ext == 'pdf':
            return await self.extract_from_pdf(file_path)
        elif ext == 'docx':
            return await self.extract_from_docx(file_path)
        elif ext == 'txt':
            return await self.extract_from_txt(file_path)
        
        return None
