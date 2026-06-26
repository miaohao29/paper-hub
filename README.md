# Paper Hub - Academic Knowledge Base System

A comprehensive platform for building, managing, and analyzing your personal academic knowledge base. Paper Hub combines document management, LLM-powered analysis, semantic search, and knowledge graph visualization to help researchers organize and discover insights from their paper collection.

## 🌟 Features

### 📚 Paper Management
- **Upload & Import**: Add papers via PDF/DOCX upload or import directly from arXiv
- **Metadata Extraction**: Automatically extract title, authors, abstract, DOI, and publication details
- **Full-Text Search**: Search across paper titles, abstracts, and content
- **Organization**: Tag papers with keywords and organize by research topics

### 🧠 LLM-Powered Analysis
- **Innovation Extraction**: Identify and extract key innovations from papers using advanced LLMs
- **Automated Summarization**: Generate concise summaries of paper content
- **Relationship Discovery**: Find connections and citations between papers
- **Comparison Analysis**: Compare multiple papers side-by-side

### 🔍 Knowledge Graph
- **Visual Exploration**: Interactive graph visualization of papers, authors, concepts, and methodologies
- **Community Detection**: Automatically identify research clusters and themes
- **Semantic Relationships**: Discover implicit connections between research areas
- **Node Navigation**: Explore neighbors and related content with one click

### 📊 Research Insights
- **Trend Analysis**: Track emerging topics and research directions
- **Timeline Visualization**: See the evolution of your research topics over time
- **Methodology Tracking**: Identify popular research methods and their adoption
- **Emerging Topics**: Discover new topics gaining research attention

### 🔎 Advanced Search
- **Semantic Search**: Find relevant papers even with different terminology
- **Citation Network**: Search papers by citations and references
- **Author Search**: Find all papers by specific authors
- **Advanced Filters**: Filter by year, venue, keywords, and more

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│           Frontend (React + TypeScript)             │
│  - Paper Management UI                              │
│  - Knowledge Graph Visualization (Sigma.js)         │
│  - Search & Analysis Interface                      │
│  - Real-time Notifications                          │
└────────────────┬────────────────────────────────────┘
                 │ HTTP/WebSocket
┌────────────────▼────────────────────────────────────┐
│         Backend API (FastAPI + Python)             │
│  - Paper Management Service                         │
│  - LLM Integration Layer                            │
│  - Vector Database & Embeddings                     │
│  - Knowledge Graph Construction                     │
│  - Search & Analysis Engine                         │
└────────────┬────────────────────┬──────────────────┘
             │                    │
    ┌────────▼────────┐  ┌────────▼──────────┐
    │  PostgreSQL DB  │  │  Redis Cache      │
    │  - Metadata     │  │  - Sessions       │
    │  - Papers       │  │  - Embeddings     │
    │  - Graph Data   │  │  - Job Queue      │
    └─────────────────┘  └───────────────────┘
             │                    │
    ┌────────▼─────────────────────▼────────┐
    │     External Services & Data           │
    │  - OpenAI / Anthropic (LLM)           │
    │  - OpenAI Embeddings                  │
    │  - arXiv API                          │
    │  - Web Scrapers                       │
    └─────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.10+ (for local development)
- Node.js 18+ (for local frontend development)
- API Keys: OpenAI (LLM + Embeddings)

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/paper-hub.git
cd paper-hub

# Create .env file
cp .env.example .env
# Edit .env and add your API keys

# Start all services
docker-compose up

# Access the application
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Local Development Setup

#### Backend
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
alembic upgrade head

# Run server
uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 📖 API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation.

### Key Endpoints

#### Papers
- `GET /api/papers` - List papers
- `POST /api/papers` - Create paper
- `POST /api/papers/upload` - Upload paper file
- `POST /api/papers/arxiv/import` - Import from arXiv
- `GET /api/papers/{id}` - Get paper details

#### Analysis
- `POST /api/analysis/{paper_id}/analyze` - Analyze paper
- `GET /api/analysis/{paper_id}/innovations` - Get innovation points
- `GET /api/analysis/{paper_id}/relationships` - Get related papers
- `POST /api/analysis/compare` - Compare multiple papers

#### Knowledge Graph
- `GET /api/graph/nodes` - Get graph nodes
- `GET /api/graph/edges` - Get graph edges
- `POST /api/graph/search` - Search graph
- `GET /api/graph/communities` - Get communities
- `GET /api/graph/insights` - Get graph insights

#### Search
- `POST /api/search` - Semantic search
- `POST /api/search/citations` - Citation search
- `POST /api/search/authors` - Author search
- `POST /api/search/advanced` - Advanced search

#### Trends
- `GET /api/trends` - Get research trends
- `GET /api/trends/topics` - Get trending topics
- `GET /api/trends/methods` - Get methodology trends
- `GET /api/trends/timeline` - Get research timeline
- `GET /api/trends/emerging` - Get emerging topics

## 🔧 Configuration

### Environment Variables

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/paper_hub

# Redis
REDIS_URL=redis://localhost:6379/0

# LLM Configuration
LLM_PROVIDER=openai  # openai, anthropic, local
LLM_API_KEY=sk-...
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.3

# Embeddings
EMBEDDING_PROVIDER=openai
EMBEDDING_API_KEY=sk-...
EMBEDDING_MODEL=text-embedding-3-small

# Vector Database
LANCEDB_PATH=./lancedb

# Frontend
VITE_API_URL=http://localhost:8000
```

## 📁 Project Structure

```
paper-hub/
├── backend/
│   ├── app/
│   │   ├── api/                 # API routes
│   │   ├── db/                  # Database models & sessions
│   │   ├── services/            # Business logic
│   │   ├── models/              # Pydantic schemas
│   │   ├── utils/               # Helper functions
│   │   ├── prompts/             # LLM prompts
│   │   ├── tasks/               # Celery tasks
│   │   └── main.py              # FastAPI app
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/          # React components
│   │   ├── pages/               # Page components
│   │   ├── hooks/               # Custom hooks
│   │   ├── stores/              # Zustand stores
│   │   ├── services/            # API services
│   │   ├── types/               # TypeScript types
│   │   ├── utils/               # Helper functions
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🛠️ Development

### Adding a New Paper Analysis Feature

1. Create a service method in `backend/app/services/analysis_service.py`
2. Add an API endpoint in `backend/app/api/analysis.py`
3. Create a React hook in `frontend/src/hooks/`
4. Build UI components in `frontend/src/components/`
5. Add page or integrate into existing page

### LLM Integration

Supports multiple LLM providers:
- **OpenAI**: Uses `openai` Python library
- **Anthropic**: Uses `anthropic` Python library  
- **Local**: Custom integration for local models

### Vector Database

Uses **LanceDB** for efficient vector storage and retrieval:
- Stores paper embeddings
- Enables semantic similarity search
- Scales to millions of vectors

## 🔐 Security

- API keys stored in environment variables
- CORS enabled for configured origins
- Database connection pooling
- Input validation on all endpoints
- Rate limiting (recommended via reverse proxy)

## 📊 Performance

- **Caching**: Redis for session and query caching
- **Async Processing**: Celery for background tasks
- **Batch Operations**: Bulk embedding generation
- **Database Indexing**: Optimized queries on frequently searched fields
- **Pagination**: Efficient data loading

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/), [React](https://react.dev/), and [Tailwind CSS](https://tailwindcss.com/)
- Vector search powered by [LanceDB](https://lancedb.com/)
- Graph visualization with [Sigma.js](https://www.sigmajs.org/)
- LLM integration with [OpenAI](https://openai.com/) and [Anthropic](https://www.anthropic.com/)

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check existing documentation
- Review API documentation at `/docs`

## 🗺️ Roadmap

- [ ] Real-time collaboration features
- [ ] Advanced visualization options
- [ ] Multi-language support
- [ ] PDF annotation and highlighting
- [ ] Research proposal generation
- [ ] Literature review automation
- [ ] Integration with Zotero and Mendeley
- [ ] Mobile app

---

**Start building your knowledge base today! 🚀**
