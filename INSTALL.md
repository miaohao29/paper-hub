# Installation & Setup Guide

## System Requirements

- **OS**: Ubuntu 20.04+, macOS 11+, Windows 10+
- **Docker**: Version 20.10+
- **Docker Compose**: Version 2.0+
- **Python**: 3.10+ (for local development)
- **Node.js**: 18+ (for local frontend development)
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 20GB minimum

## Quick Start (5 minutes)

### Using Docker Compose

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/paper-hub.git
   cd paper-hub
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your API keys:
   ```bash
   LLM_API_KEY=sk-your-openai-key
   EMBEDDING_API_KEY=sk-your-embedding-key
   ```

3. **Start services**
   ```bash
   docker-compose up
   ```

4. **Access the application**
   - **Frontend**: http://localhost:5173
   - **Backend API**: http://localhost:8000
   - **API Docs**: http://localhost:8000/docs

## Detailed Setup

### Backend Setup (Local Development)

#### 1. Install Python Dependencies
```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

#### 2. Database Setup
```bash
# Make sure PostgreSQL is running
# On Linux:
sudo systemctl start postgresql
# On macOS with Homebrew:
brew services start postgresql
# On Windows: Start PostgreSQL service

# Create database and user (if not using docker)
psql -U postgres
CREATE DATABASE paper_hub;
CREATE USER paper_hub WITH PASSWORD 'your_password';
ALTER ROLE paper_hub SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE paper_hub TO paper_hub;

# Run migrations
cd backend
alembic upgrade head
```

#### 3. Configure Environment
```bash
cd backend
cp .env.example .env
```

Edit `.env`:
```bash
DATABASE_URL=postgresql://paper_hub:your_password@localhost:5432/paper_hub
REDIS_URL=redis://localhost:6379/0
LLM_API_KEY=sk-your-key
EMBEDDING_API_KEY=sk-your-key
```

#### 4. Start Backend
```bash
cd backend
uvicorn app.main:app --reload
```

The backend will be available at `http://localhost:8000`

### Frontend Setup (Local Development)

#### 1. Install Dependencies
```bash
cd frontend
npm install
```

#### 2. Configure Environment
```bash
cd frontend
cp .env.example .env
```

Edit `.env`:
```bash
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000
```

#### 3. Start Development Server
```bash
cd frontend
npm run dev
```

The frontend will be available at `http://localhost:5173`

## External Service Setup

### OpenAI API

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or login
3. Navigate to [API Keys](https://platform.openai.com/account/api-keys)
4. Create new secret key
5. Add to `.env`:
   ```bash
   LLM_API_KEY=sk-...
   EMBEDDING_API_KEY=sk-...
   ```

### Anthropic API (Optional)

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Create account and verify email
3. Navigate to API Keys
4. Create new key
5. Add to `.env`:
   ```bash
   LLM_PROVIDER=anthropic
   LLM_API_KEY=your-anthropic-key
   ```

## Docker Setup

### Build Images
```bash
# Build specific service
docker-compose build backend
docker-compose build frontend

# Build all services
docker-compose build
```

### Run Services
```bash
# Start all services
docker-compose up

# Start in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Remove volumes
docker-compose down -v
```

### Database Management

```bash
# Enter database container
docker-compose exec postgres psql -U paper_hub -d paper_hub

# Run migrations
docker-compose exec backend alembic upgrade head

# Create backup
docker-compose exec postgres pg_dump -U paper_hub paper_hub > backup.sql

# Restore backup
docker-compose exec -T postgres psql -U paper_hub paper_hub < backup.sql
```

## Verification

### Test Backend
```bash
# Check health endpoint
curl http://localhost:8000/health

# Response should be:
# {"status":"healthy","version":"0.1.0"}
```

### Test API
```bash
# Get all papers
curl http://localhost:8000/api/papers

# View API docs
# Open http://localhost:8000/docs
```

### Test Frontend
```bash
# Should see login/dashboard page at:
# http://localhost:5173
```

## Common Issues & Solutions

### "Connection refused" for database
- **Cause**: PostgreSQL not running
- **Solution**: 
  ```bash
  # Linux
  sudo systemctl start postgresql
  # macOS
  brew services start postgresql
  ```

### "Port already in use"
- **Cause**: Another service using the port
- **Solution**:
  ```bash
  # Find process using port 8000
  lsof -i :8000
  # Kill the process
  kill -9 <PID>
  ```

### "Module not found" Python error
- **Cause**: Virtual environment not activated or dependencies not installed
- **Solution**:
  ```bash
  source venv/bin/activate  # or venv\Scripts\activate on Windows
  pip install -r requirements.txt
  ```

### "npm ERR!" during frontend build
- **Cause**: Dependency conflict or outdated node modules
- **Solution**:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  npm run build
  ```

### API key errors
- **Cause**: Invalid or missing API keys
- **Solution**:
  - Verify API key format in `.env`
  - Check API key is active in provider account
  - Ensure environment variables are loaded

## Next Steps

1. **Upload Your First Paper**
   - Go to http://localhost:5173/papers
   - Click "Add Paper"
   - Upload a PDF or enter an arXiv ID

2. **Explore Features**
   - View Knowledge Graph: http://localhost:5173/graph
   - Analyze Trends: http://localhost:5173/trends
   - Search Papers: http://localhost:5173/search

3. **Customize Settings**
   - Configure LLM model in Settings
   - Adjust analysis parameters
   - Set up notifications

## Support & Resources

- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check DEVELOPMENT.md for detailed guides
- **API Docs**: http://localhost:8000/docs
- **Community**: Discussions and Q&A

## Production Deployment

For production deployment, see [DEPLOYMENT.md](DEPLOYMENT.md) (to be created).

---

**Need help? Open an issue on GitHub!**
