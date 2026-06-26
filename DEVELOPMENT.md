# Paper Hub Development Guide

## Project Overview

Paper Hub is an academic knowledge base system that combines paper management, LLM-powered analysis, semantic search, and knowledge graph visualization. This guide covers the development setup, architecture, and contribution guidelines.

## Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **Cache**: Redis
- **Vector DB**: LanceDB
- **Task Queue**: Celery
- **LLM Integration**: OpenAI, Anthropic
- **Document Processing**: PyPDF2, python-docx

### Frontend
- **Framework**: React 19 + TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Graph Visualization**: Sigma.js
- **HTTP Client**: Axios
- **Build Tool**: Vite

## Development Environment Setup

### Backend Setup

```bash
# Clone repository
git clone https://github.com/yourusername/paper-hub.git
cd paper-hub/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
cp .env.example .env
# Edit .env with your settings
alembic upgrade head

# Run server
uvicorn app.main:app --reload
# Server will be available at http://localhost:8000
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
# Frontend will be available at http://localhost:5173
```

## Database Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1
```

## Code Style & Linting

### Backend
```bash
# Format code
black app/

# Sort imports
isort app/

# Lint code
flake8 app/

# Type checking
mypy app/
```

### Frontend
```bash
# Format code
npm run format

# Lint code
npm run lint

# Type check
npm run type-check
```

## Project Structure Details

### Backend Structure

```
backend/
├── app/
│   ├── api/
│   │   ├── papers.py          # Paper CRUD endpoints
│   │   ├── analysis.py        # Paper analysis endpoints
│   │   ├── knowledge_graph.py # Graph endpoints
│   │   ├── search.py          # Search endpoints
│   │   └── trends.py          # Trend analysis endpoints
│   ├── db/
│   │   ├── database.py        # DB connection & session
│   │   ├── base.py            # Base model mixins
│   │   └── models.py          # SQLAlchemy models
│   ├── services/
│   │   ├── paper_service.py   # Paper business logic
│   │   ├── analysis_service.py# Analysis logic
│   │   ├── search_service.py  # Search logic
│   │   ├── graph_service.py   # Graph logic
│   │   ├── llm_service.py     # LLM integration
│   │   ├── embedding_service.py# Vector operations
│   │   └── extraction_service.py# Document extraction
│   ├── models/
│   │   └── schemas.py         # Pydantic schemas
│   ├── utils/
│   │   ├── validators.py      # Input validation
│   │   ├── arxiv_fetcher.py   # arXiv API client
│   │   ├── date.py            # Date utilities
│   │   └── format.py          # Formatting utilities
│   ├── tasks/
│   │   ├── celery_app.py      # Celery configuration
│   │   └── tasks.py           # Async tasks
│   ├── prompts/
│   │   ├── paper_analysis.txt # Analysis prompts
│   │   ├── innovation_extraction.txt
│   │   └── trend_analysis.txt
│   ├── config.py              # Settings
│   └── main.py                # FastAPI app entry
├── requirements.txt
├── Dockerfile
└── .env.example
```

### Frontend Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── common/
│   │   │   ├── Header.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   └── LoadingSpinner.tsx
│   │   ├── papers/
│   │   │   ├── PaperList.tsx
│   │   │   ├── PaperCard.tsx
│   │   │   ├── PaperUpload.tsx
│   │   │   ├── PaperFilters.tsx
│   │   │   └── PaperDetailView.tsx
│   │   ├── graph/
│   │   │   └── KnowledgeGraph.tsx
│   │   ├── analysis/
│   │   │   └── InnovationPoints.tsx
│   │   ├── trends/
│   │   │   └── TrendAnalysis.tsx
│   │   └── search/
│   │       └── SearchBar.tsx
│   ├── pages/
│   │   ├── Dashboard.tsx
│   │   ├── Papers.tsx
│   │   ├── PaperDetail.tsx
│   │   ├── Graph.tsx
│   │   ├── Analysis.tsx
│   │   ├── Trends.tsx
│   │   ├── Search.tsx
│   │   └── Settings.tsx
│   ├── hooks/
│   │   ├── usePapers.ts
│   │   ├── useGraph.ts
│   │   └── useSearch.ts
│   ├── stores/
│   │   ├── paperStore.ts      # Zustand paper store
│   │   ├── graphStore.ts      # Zustand graph store
│   │   └── uiStore.ts         # Zustand UI store
│   ├── services/
│   │   └── api.ts             # API client
│   ├── types/
│   │   ├── paper.ts
│   │   ├── graph.ts
│   │   └── trend.ts
│   ├── utils/
│   │   ├── date.ts
│   │   ├── format.ts
│   │   └── colors.ts
│   ├── contexts/
│   │   └── ToastContext.tsx
│   ├── styles/
│   │   └── globals.css
│   ├── App.tsx
│   └── main.tsx
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
└── Dockerfile
```

## Adding New Features

### Adding a New Paper Analysis Feature

1. **Create Database Model** (if needed)
   ```python
   # backend/app/db/models.py
   class MyAnalysis(BaseMixin, Base):
       __tablename__ = "my_analysis"
       paper_id = Column(String(36), ForeignKey('papers.id'))
       result = Column(JSON)
   ```

2. **Create Pydantic Schema**
   ```python
   # backend/app/models/schemas.py
   class MyAnalysisResponse(BaseModel):
       id: str
       paper_id: str
       result: dict
   ```

3. **Create Service Method**
   ```python
   # backend/app/services/analysis_service.py
   async def my_analysis(self, db: Session, paper_id: str):
       # Implementation
       pass
   ```

4. **Add API Endpoint**
   ```python
   # backend/app/api/analysis.py
   @router.post("/{paper_id}/my_analysis")
   async def get_my_analysis(paper_id: str, db: Session = Depends(get_db)):
       result = await analysis_service.my_analysis(db, paper_id)
       return result
   ```

5. **Create React Hook**
   ```typescript
   // frontend/src/hooks/useMyAnalysis.ts
   export const useMyAnalysis = (paperId: string) => {
     const [data, setData] = useState(null)
     // Implementation
   }
   ```

6. **Create React Component**
   ```typescript
   // frontend/src/components/analysis/MyAnalysis.tsx
   export const MyAnalysis = ({ paperId }: { paperId: string }) => {
     const { data } = useMyAnalysis(paperId)
     // Render component
   }
   ```

## Testing

### Backend Testing
```bash
# Run tests
pytest

# Run specific test
pytest tests/test_papers.py

# Run with coverage
pytest --cov=app
```

### Frontend Testing
```bash
# Run tests (if configured)
npm test
```

## Deployment

### Docker Compose Deployment
```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Considerations
- Use strong database passwords
- Enable HTTPS/TLS
- Configure proper CORS origins
- Set up proper logging and monitoring
- Use environment variables for sensitive data
- Configure rate limiting
- Set up backup strategy for database

## Troubleshooting

### Database Connection Issues
```bash
# Check if PostgreSQL is running
psql -U paper_hub -d paper_hub -h localhost

# Check database URL format
# postgresql://user:password@host:port/database
```

### API Connection Issues
```bash
# Check if backend is running
curl http://localhost:8000/health

# Check CORS settings in .env
```

### Frontend Build Issues
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm run build
```

## Performance Optimization

### Backend
- Add database indexes on frequently queried fields
- Use connection pooling
- Implement caching for repeated queries
- Use async operations for I/O
- Batch embedding generation

### Frontend
- Code splitting by route
- Lazy loading components
- Image optimization
- State management optimization
- Memoization of expensive computations

## Contributing Guidelines

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes
3. Run linting and tests
4. Commit with clear messages
5. Push to your fork
6. Create a Pull Request

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [LanceDB Documentation](https://lancedb.com/docs)

---

For questions or issues, please open a GitHub issue or discussion.
