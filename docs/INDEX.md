# Paper Hub

A comprehensive academic knowledge base system combining paper management, LLM-powered analysis, semantic search, and knowledge graph visualization.

## 🚀 Quick Links

- **[Installation Guide](INSTALL.md)** - Get started in 5 minutes
- **[Development Guide](DEVELOPMENT.md)** - For developers and contributors
- **[API Documentation](http://localhost:8000/docs)** - Swagger UI (when running)
- **[GitHub](https://github.com/yourusername/paper-hub)** - Source code

## 📚 Documentation

### Getting Started
1. [Installation & Setup](INSTALL.md)
2. [Docker Setup](INSTALL.md#docker-setup)
3. [Configuration](INSTALL.md#external-service-setup)

### Development
1. [Development Setup](DEVELOPMENT.md#development-environment-setup)
2. [Project Structure](DEVELOPMENT.md#project-structure-details)
3. [Adding Features](DEVELOPMENT.md#adding-new-features)
4. [Testing](DEVELOPMENT.md#testing)

### Features
- [Paper Management](README.md#-paper-management)
- [LLM-Powered Analysis](README.md#-llm-powered-analysis)
- [Knowledge Graph](README.md#-knowledge-graph)
- [Research Insights](README.md#-research-insights)
- [Advanced Search](README.md#-advanced-search)

## 🛠️ Tech Stack

**Backend**: FastAPI, PostgreSQL, Redis, LanceDB
**Frontend**: React, TypeScript, Tailwind CSS, Sigma.js
**LLM**: OpenAI / Anthropic

## 📖 Full Documentation

See [README.md](README.md) for complete documentation.

## 💡 Quick Examples

### Upload a Paper
```bash
curl -X POST http://localhost:8000/api/papers/upload \
  -F "file=@paper.pdf"
```

### Semantic Search
```bash
curl -X POST http://localhost:8000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "machine learning", "limit": 20}'
```

### Analyze a Paper
```bash
curl -X POST http://localhost:8000/api/analysis/PAPER_ID/analyze
```

## 🤝 Contributing

Contributions welcome! See [DEVELOPMENT.md](DEVELOPMENT.md#contributing-guidelines)

## 📄 License

MIT License - See LICENSE file

## 📞 Support

- Open an issue on GitHub
- Check existing documentation
- Review API docs at `/docs`

---

**[→ Start Getting Started](INSTALL.md)**
