# Paper Hub 🎓

An intelligent academic knowledge base system for managing research papers, discovering innovation points, exploring paper relationships, and identifying future research directions.

Based on the proven LLM Wiki pattern, optimized specifically for academic research.

## Overview

Paper Hub transforms your research paper collection into a living knowledge base:
- **Paper Ingestion**: Automatically extract metadata, abstracts, and key insights from papers
- **Innovation Analysis**: AI-powered analysis of novel contributions and research innovations
- **Relationship Mapping**: Build knowledge graphs connecting papers, authors, concepts, and methodologies
- **Future Trends**: Identify emerging research directions and knowledge gaps
- **Multi-format Support**: Handle PDF, DOCX, arXiv links, and metadata files
- **Semantic Search**: Vector-based similarity search across your paper collection
- **Research Insights**: Auto-generate summaries of research areas and trends

## Tech Stack

### Backend
- **Python 3.10+**
- **FastAPI**: High-performance REST API
- **PostgreSQL**: Structured data storage
- **LanceDB**: Vector database for semantic search
- **Celery + Redis**: Asynchronous task processing
- **LLM Integration**: OpenAI, Claude, Local LLMs
- **SQLAlchemy**: ORM
- **Alembic**: Database migrations

### Frontend
- **React 19**: Modern UI framework
- **TypeScript**: Type-safe development
- **Vite**: Fast build tool
- **TailwindCSS + shadcn/ui**: Professional UI components
- **Zustand**: State management
- **sigma.js + graphology**: Knowledge graph visualization
- **ForceAtlas2**: Graph layout algorithm

## Project Structure

```
paper-hub/
├── backend/                          # Python FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                   # FastAPI application entry
│   │   ├── config.py                 # Configuration & settings
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── papers.py             # Paper CRUD endpoints
│   │   │   ├── analysis.py           # Analysis endpoints
│   │   │   ├── knowledge_graph.py    # Graph visualization endpoints
│   │   │   ├── search.py             # Search endpoints
│   │   │   └── trends.py             # Trend analysis endpoints
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── paper_service.py      # Paper management logic
│   │   │   ├── llm_service.py        # LLM integration
│   │   │   ├── analysis_service.py   # Paper analysis
│   │   │   ├── extraction_service.py # PDF/DOCX extraction
│   │   │   ├── graph_service.py      # Knowledge graph construction
│   │   │   ├── search_service.py     # Semantic search
│   │   │   ├── embedding_service.py  # Vector embeddings
│   │   │   └── arxiv_service.py      # arXiv fetching
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── paper.py              # SQLAlchemy Paper model
│   │   │   ├── analysis.py           # Analysis model
│   │   │   ├── graph.py              # Graph models
│   │   │   └── schemas.py            # Pydantic schemas
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── database.py           # Database connection
│   │   │   ├── base.py               # Base model
│   │   │   ├── models.py             # All SQLAlchemy models
│   │   │   └── migrations/
│   │   │       ├── env.py
│   │   │       ├── script.py.mako
│   │   │       └── versions/
│   │   ├── tasks/
│   │   │   ├── __init__.py
│   │   │   ├── paper_ingest.py       # Paper ingestion tasks
│   │   │   ├── analysis_tasks.py     # Analysis tasks
│   │   │   ├── embedding_tasks.py    # Embedding tasks
│   │   │   └── celery_app.py         # Celery configuration
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── pdf_processor.py      # PDF extraction
│   │   │   ├── docx_processor.py     # DOCX extraction
│   │   │   ├── arxiv_fetcher.py      # arXiv API
│   │   │   └── validators.py         # Input validation
│   │   ├── prompts/
│   │   │   ├── paper_analysis.txt
│   │   │   ├── innovation_extraction.txt
│   │   │   ├── trend_analysis.txt
│   │   │   └── relationship_analysis.txt
│   │   └── middleware/
│   │       ├── __init__.py
│   │       └── auth.py               # Authentication
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_papers.py
│   │   ├── test_analysis.py
│   │   └── test_search.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── Dockerfile
│   ├── alembic.ini
│   └── run.sh
│
├── frontend/                         # React TypeScript frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── Header.tsx
│   │   │   │   ├── Sidebar.tsx
│   │   │   │   ├── LoadingSpinner.tsx
│   │   │   │   └── ErrorBoundary.tsx
│   │   │   ├── papers/
│   │   │   │   ├── PaperUpload.tsx
│   │   │   │   ├── PaperList.tsx
│   │   │   │   ├── PaperDetail.tsx
│   │   │   │   ├── PaperCard.tsx
│   │   │   │   └── PaperFilters.tsx
│   │   │   ├── analysis/
│   │   │   │   ├── InnovationPoints.tsx
│   │   │   │   ├── PaperComparison.tsx
│   │   │   │   ├── AnalysisPanel.tsx
│   │   │   │   └── RelationshipAnalysis.tsx
│   │   │   ├── graph/
│   │   │   │   ├── KnowledgeGraph.tsx
│   │   │   │   ├── GraphControls.tsx
│   │   │   │   ├── GraphLegend.tsx
│   │   │   │   └── GraphInsights.tsx
│   │   │   ├── search/
│   │   │   │   ├── SearchBar.tsx
│   │   │   │   ├── SearchResults.tsx
│   │   │   │   └── AdvancedSearch.tsx
│   │   │   └── trends/
│   │   │       ├── TrendAnalysis.tsx
│   │   │       ├── ResearchTimeline.tsx
│   │   │       ├── EmergingTopics.tsx
│   │   │       └── TrendChart.tsx
│   │   ├── pages/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Papers.tsx
│   │   │   ├── PaperDetail.tsx
│   │   │   ├── Graph.tsx
│   │   │   ├── Analysis.tsx
│   │   │   ├── Trends.tsx
│   │   │   ├── Search.tsx
│   │   │   └── Settings.tsx
│   │   ├── services/
│   │   │   ├── api.ts                # API client
│   │   │   ├── websocket.ts          # WebSocket service
│   │   │   └── storage.ts            # Local storage
│   │   ├── stores/
│   │   │   ├── paperStore.ts         # Zustand store for papers
│   │   │   ├── graphStore.ts         # Zustand store for graphs
│   │   │   ├── uiStore.ts            # UI state
│   │   │   └── analysisStore.ts      # Analysis state
│   │   ├── types/
│   │   │   ├── paper.ts              # Paper types
│   │   │   ├── analysis.ts           # Analysis types
│   │   │   ├── graph.ts              # Graph types
│   │   │   ├── trend.ts              # Trend types
│   │   │   └── api.ts                # API types
│   │   ├── utils/
│   │   │   ├── format.ts
│   │   │   ├── date.ts
│   │   │   ├── colors.ts
│   │   │   └── validators.ts
│   │   ├── hooks/
│   │   │   ├── usePapers.ts
│   │   │   ├── useGraph.ts
│   │   │   ├── useSearch.ts
│   │   │   └── useAnalysis.ts
│   │   ├── styles/
│   │   │   ├── globals.css
│   │   │   └── theme.css
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── public/
│   │   ├── logo.png
│   │   └── favicon.ico
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── .eslintrc.json
│
├── knowledge_base/                   # Knowledge base structure
│   ├── raw/
│   │   └── papers/                   # Raw paper files
│   ├── wiki/
│   │   ├── index.md                  # Content catalog
│   │   ├── overview.md               # Global summary
│   │   ├── papers/                   # Paper summaries
│   │   ├── innovations/              # Innovation points
│   │   ├── researchers/              # Author profiles
│   │   ├── methodologies/            # Techniques & methods
│   │   ├── datasets/                 # Research datasets
│   │   ├── trends/                   # Research trends
│   │   ├── future_directions/        # Future research areas
│   │   └── synthesis/                # Cross-paper analysis
│   ├── purpose.md                    # Knowledge base goals
│   └── schema.md                     # Wiki structure rules
│
├── docker-compose.yml                # Docker Compose for local development
├── .gitignore
├── LICENSE                           # MIT License
└── SETUP.md                          # Setup guide
```

## Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL 14+
- Redis 7+
- Docker & Docker Compose (optional)

### Option 1: Docker Compose (Recommended)

```bash
# Clone repository
git clone https://github.com/miaohao29/paper-hub.git
cd paper-hub

# Start all services
docker-compose up -d

# Access applications
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Manual Setup

#### Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your configuration

# Initialize database
alembic upgrade head

# Start server
uvicorn app.main:app --reload --port 8000
```

#### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be available at `http://localhost:5173`

## Key Features

### 📄 Paper Management
- Upload PDF, DOCX papers
- Fetch from arXiv by ID or DOI
- Auto-extract metadata (title, authors, abstract, keywords, publication date)
- Support for paper notes and annotations
- Batch import functionality
- Paper versioning

### 🔬 Innovation Analysis
- Identify key contributions and novelty
- Extract novel methodologies
- Compare with related work (state-of-the-art)
- Assess innovation significance and impact
- Innovation timeline visualization
- Research gap identification

### 🕸️ Knowledge Graph
- Paper relationships (citations, similar topics, methodologies)
- Author connections and collaboration networks
- Research methodology networks
- Concept hierarchies and taxonomies
- Graph visualization with interactive exploration
- Community detection and clustering
- Bridge node identification

### 📊 Research Insights
- Identify knowledge gaps in research areas
- Discover emerging trends and hot topics
- Track research evolution over time
- Predict future research directions
- Automatic summary generation
- Research area benchmarking

### 🔍 Semantic Search
- Vector-based similarity search using embeddings
- Multi-modal search (papers, innovations, authors, trends)
- Filter by author, year, topic, methodology
- Citation network traversal
- Full-text search with highlighting
- Advanced query syntax

### 📈 Trend Analysis
- Research topic trends over time
- Emerging methodology adoption
- Author productivity trends
- Collaboration patterns
- Publication venue trends
- Hot topics identification

## API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive Swagger documentation.

### Main Endpoints

**Papers**
```
GET    /api/papers              - List all papers
POST   /api/papers              - Upload paper
GET    /api/papers/{paper_id}   - Get paper details
PUT    /api/papers/{paper_id}   - Update paper
DELETE /api/papers/{paper_id}   - Delete paper
POST   /api/papers/arxiv        - Import from arXiv
```

**Analysis**
```
POST   /api/papers/{paper_id}/analyze        - Analyze paper
GET    /api/papers/{paper_id}/innovations    - Get innovation points
GET    /api/papers/{paper_id}/relationships  - Get related papers
POST   /api/analysis/compare                 - Compare papers
```

**Knowledge Graph**
```
GET    /api/graph/nodes         - Get all nodes
GET    /api/graph/edges         - Get all relationships
POST   /api/graph/search        - Search graph
GET    /api/graph/communities   - Get communities
GET    /api/graph/insights      - Get insights
```

**Search**
```
POST   /api/search              - Semantic search
POST   /api/search/citations    - Citation search
POST   /api/search/authors      - Author search
POST   /api/search/advanced     - Advanced search
```

**Trends**
```
GET    /api/trends              - Get all trends
GET    /api/trends/topics       - Topic trends
GET    /api/trends/methods      - Methodology trends
GET    /api/trends/timeline     - Timeline analysis
```

## Environment Variables

Create `.env` file in `backend/` directory:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/paper_hub

# Redis
REDIS_URL=redis://localhost:6379/0

# LLM Configuration
LLM_PROVIDER=openai              # Options: openai, anthropic, local
LLM_API_KEY=your_api_key_here
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.3
LLM_MAX_TOKENS=2000

# Embedding Configuration
EMBEDDING_PROVIDER=openai
EMBEDDING_API_KEY=your_api_key_here
EMBEDDING_MODEL=text-embedding-3-small

# Vector Database
LANCEDB_PATH=./lancedb

# Frontend
FRONTEND_URL=http://localhost:5173

# File Upload
UPLOAD_DIR=./uploads
MAX_FILE_SIZE=100MB

# API
API_PORT=8000
API_HOST=0.0.0.0

# Logging
LOG_LEVEL=INFO

# arXiv
ARXIV_ENABLED=true
ARXIV_RATE_LIMIT=5  # requests per second
```

## Development

### Running Tests

```bash
# Backend tests
cd backend
pytest -v

# Frontend tests
cd frontend
npm test

# Coverage
cd backend
pytest --cov=app
```

### Code Quality

```bash
# Python
cd backend
black app/
flake8 app/ --max-line-length=100
mypy app/
isort app/

# TypeScript
cd frontend
npm run lint
npm run format
npm run type-check
```

### Database Migrations

```bash
cd backend

# Create migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Downgrade
alembic downgrade -1
```

## Project Customization

### Configure LLM Provider

Edit `backend/app/config.py` to set your preferred LLM:

```python
# OpenAI
LLM_PROVIDER = "openai"
LLM_MODEL = "gpt-4"

# Anthropic
LLM_PROVIDER = "anthropic"
LLM_MODEL = "claude-3-opus"

# Local (Ollama)
LLM_PROVIDER = "local"
LLM_BASE_URL = "http://localhost:11434"
LLM_MODEL = "llama2"
```

### Configure Embedding Model

Edit `backend/app/config.py`:

```python
EMBEDDING_MODEL = "text-embedding-3-small"  # OpenAI
EMBEDDING_MODEL = "all-MiniLM-L6-v2"       # Open source
```

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│          Frontend (React + TypeScript)          │
│  Papers | Graph | Analysis | Search | Trends   │
└──────────────────┬──────────────────────────────┘
                   │ HTTP/WebSocket
┌──────────────────▼──────────────────────────────┐
│         FastAPI Backend (Python)                │
│  REST API | WebSocket | Task Queue             │
└────┬────────────────────────────────────┬───────┘
     │                                    │
  ┌──▼──────────┐    ┌──────────────┐  ┌─▼──────────────┐
  │ PostgreSQL  │    │ LanceDB      │  │ Redis + Celery │
  │ (Metadata)  │    │ (Embeddings) │  │ (Tasks)        │
  └─────────────┘    └──────────────┘  └────────────────┘
     │
  ┌──▼────────────────┐
  │ LLM Services      │
  │ • OpenAI/Claude   │
  │ • Analysis        │
  │ • Embeddings      │
  └───────────────────┘
```

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write/update tests
5. Run code quality checks
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details

## Citation

Based on the LLM Wiki pattern by [Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and the [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki) implementation.

## Acknowledgments

- Andrej Karpathy for the LLM Wiki pattern
- nashsu for the comprehensive LLM Wiki implementation
- All contributors to the paper-hub project

## Support

For questions or suggestions:
- Open an [Issue](https://github.com/miaohao29/paper-hub/issues)
- Check [Discussions](https://github.com/miaohao29/paper-hub/discussions)
- Read [Documentation](./SETUP.md)

## Roadmap

- [ ] Multi-language support (Chinese, Japanese, Korean)
- [ ] Advanced graph visualization (3D, force-directed layout)
- [ ] Paper recommendation engine
- [ ] Collaborative features for teams
- [ ] Mobile app
- [ ] Export to Obsidian, Notion, Zotero
- [ ] Integration with arXiv, PubMed, DOI APIs
- [ ] Citation analysis tools
- [ ] Research proposal generation
- [ ] PDF annotation tools
