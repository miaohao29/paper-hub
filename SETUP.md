# Paper Hub - Setup Guide

## Prerequisites

- Python 3.10 or higher
- Node.js 18 or higher
- PostgreSQL 14 or higher
- Redis 7 or higher
- Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/miaohao29/paper-hub.git
cd paper-hub
```

### 2. Using Docker Compose (Recommended)

```bash
# Build and start all services
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop services
docker-compose down
```

Access the application:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### 3. Manual Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env

# Edit .env with your configuration
# Required:
# - DATABASE_URL (PostgreSQL connection string)
# - REDIS_URL (Redis connection string)
# - LLM_API_KEY (Your LLM provider API key)

# Initialize database
alembic upgrade head

# Create uploads directory
mkdir -p uploads

# Start backend server
uvicorn app.main:app --reload --port 8000
```

In another terminal, start Celery worker:

```bash
cd backend
source venv/bin/activate
celery -A app.tasks.celery_app worker --loglevel=info
```

Optionally, start Celery Beat for scheduled tasks:

```bash
cd backend
source venv/bin/activate
celery -A app.tasks.celery_app beat --loglevel=info
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at http://localhost:5173

## Configuration

### Backend Configuration

Create `backend/.env` file:

```env
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/paper_hub
DATABASE_POOL_SIZE=20

# Redis Configuration
REDIS_URL=redis://localhost:6379/0

# LLM Configuration
LLM_PROVIDER=openai  # Options: openai, anthropic, local
LLM_API_KEY=sk-...
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.3
LLM_MAX_TOKENS=2000
LLM_TIMEOUT=60

# Embedding Configuration
EMBEDDING_PROVIDER=openai
EMBEDDING_API_KEY=sk-...
EMBEDDING_MODEL=text-embedding-3-small
EMBEDDING_BATCH_SIZE=100

# Vector Database
LANCEDB_PATH=./lancedb

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4
CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000"]

# File Upload
UPLOAD_DIR=./uploads
MAX_FILE_SIZE=104857600  # 100MB in bytes
ALLOWED_EXTENSIONS=["pdf", "docx", "txt", "md"]

# arXiv Configuration
ARXIV_ENABLED=true
ARXIV_RATE_LIMIT=5  # requests per second

# Logging
LOG_LEVEL=INFO
LOG_DIR=./logs

# Frontend URL
FRONTEND_URL=http://localhost:5173
```

### Frontend Configuration

Create `frontend/.env` file:

```env
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000
VITE_ENVIRONMENT=development
```

## Database Setup

### Create Database

```bash
# Using psql
psql -U postgres
CREATE DATABASE paper_hub OWNER user;
\q
```

### Run Migrations

```bash
cd backend
alembic upgrade head
```

### Create New Migration

```bash
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

## API Keys Setup

### OpenAI API

1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Add to `.env`:
   ```
   LLM_API_KEY=sk-...
   EMBEDDING_API_KEY=sk-...
   ```

### Anthropic API

1. Go to https://console.anthropic.com/
2. Create a new API key
3. Add to `.env`:
   ```
   LLM_PROVIDER=anthropic
   LLM_API_KEY=sk-ant-...
   ```

### Local LLM (Ollama)

1. Install Ollama from https://ollama.ai
2. Run a model: `ollama run llama2`
3. Add to `.env`:
   ```
   LLM_PROVIDER=local
   LLM_BASE_URL=http://localhost:11434
   LLM_MODEL=llama2
   ```

## Testing

### Run Backend Tests

```bash
cd backend
pytest -v
pytest --cov=app  # With coverage
```

### Run Frontend Tests

```bash
cd frontend
npm test
```

## Troubleshooting

### Database Connection Error

```bash
# Check PostgreSQL is running
psql -U user -h localhost -d paper_hub

# If connection fails, check:
# 1. PostgreSQL is installed and running
# 2. DATABASE_URL is correct in .env
# 3. Database exists: CREATE DATABASE paper_hub;
```

### Redis Connection Error

```bash
# Check Redis is running
redis-cli ping

# If connection fails, check:
# 1. Redis is installed and running
# 2. REDIS_URL is correct in .env
```

### Port Already in Use

```bash
# Change port in .env:
API_PORT=8001  # Instead of 8000

# Or kill the process using the port:
# On macOS/Linux:
lsof -ti:8000 | xargs kill -9

# On Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Memory Issues

```bash
# Docker compose memory limit
# Edit docker-compose.yml:
memory: 2g

# Or use smaller models:
LLM_MODEL=gpt-3.5-turbo
EMBEDDING_MODEL=text-embedding-3-small
```

## Development

### Backend Development

```bash
cd backend
source venv/bin/activate

# Code formatting
black app/

# Linting
flake8 app/ --max-line-length=100

# Type checking
mypy app/

# Import sorting
isort app/
```

### Frontend Development

```bash
cd frontend

# Linting
npm run lint

# Formatting
npm run format

# Type checking
npm run type-check

# Build for production
npm run build
```

## Production Deployment

### Using Docker

```bash
# Build images
docker-compose build

# Start in production mode
docker-compose -f docker-compose.yml up -d
```

### Using Traditional Server

```bash
# Backend
cd backend
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Frontend
cd frontend
npm run build
npm install -g serve
serve -s dist -l 3000
```

### Using Nginx

```nginx
upstream backend {
    server localhost:8000;
}

server {
    listen 80;
    server_name your-domain.com;

    location /api {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        root /path/to/frontend/dist;
        try_files $uri /index.html;
    }
}
```

## Next Steps

1. Upload your first paper
2. Configure your LLM provider in Settings
3. Run paper analysis to extract insights
4. Explore the knowledge graph
5. Search papers using semantic search
6. Analyze research trends

## Support

For issues or questions:
- Check [GitHub Issues](https://github.com/miaohao29/paper-hub/issues)
- Read the [main README](./README.md)
- Open a new issue with details
