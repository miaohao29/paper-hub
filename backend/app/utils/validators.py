"""Input Validators"""

from app.config import get_settings

settings = get_settings()


def validate_file(filename: str) -> bool:
    """Validate uploaded file"""
    if not filename:
        return False
    
    ext = filename.split('.')[-1].lower()
    return ext in settings.allowed_extensions


def validate_email(email: str) -> bool:
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_doi(doi: str) -> bool:
    """Validate DOI format"""
    import re
    pattern = r'^10\.[0-9]{4,}\.[0-9a-zA-Z/_-]+$'
    return re.match(pattern, doi) is not None
