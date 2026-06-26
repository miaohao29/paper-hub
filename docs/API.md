# API Reference

## Base URL
```
http://localhost:8000/api
```

## Authentication

Currently, the API does not require authentication. In production, implement:
- API Key authentication
- JWT tokens
- OAuth 2.0

## Response Format

All responses are JSON:
```json
{
  "status": "success",
  "data": { /* ... */ },
  "error": null
}
```

## Error Handling

Errors follow HTTP status codes:
- `200` - OK
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `404` - Not Found
- `500` - Server Error

## Endpoints

### Papers

#### List Papers
```
GET /papers?skip=0&limit=20&search=query
```

Response:
```json
{
  "papers": [
    {
      "id": "uuid",
      "title": "Paper Title",
      "abstract": "...",
      "authors": [...],
      "keywords": [...],
      "publication_year": 2024,
      "doi": "10.xxxx/xxxx",
      "arxiv_id": "2401.xxxxx"
    }
  ],
  "total": 100,
  "skip": 0,
  "limit": 20
}
```

#### Create Paper
```
POST /papers
Content-Type: application/json

{
  "title": "Paper Title",
  "abstract": "...",
  "authors": [{"name": "..."}],
  "keywords": ["keyword1", "keyword2"]
}
```

#### Upload Paper File
```
POST /papers/upload
Content-Type: multipart/form-data

file: <binary PDF or DOCX>
```

#### Get Paper
```
GET /papers/{paper_id}
```

#### Update Paper
```
PUT /papers/{paper_id}
Content-Type: application/json

{
  "title": "Updated Title"
}
```

#### Delete Paper
```
DELETE /papers/{paper_id}
```

#### Import from arXiv
```
POST /papers/arxiv/import
Content-Type: application/json

{
  "arxiv_id": "2301.00001"
}
```

### Analysis

#### Analyze Paper
```
POST /analysis/{paper_id}/analyze
```

#### Get Innovations
```
GET /analysis/{paper_id}/innovations
```

#### Get Relationships
```
GET /analysis/{paper_id}/relationships
```

#### Compare Papers
```
POST /analysis/compare
Content-Type: application/json

{
  "paper_ids": ["id1", "id2", "id3"]
}
```

### Knowledge Graph

#### Get Nodes
```
GET /graph/nodes?node_type=paper
```

#### Get Edges
```
GET /graph/edges
```

#### Search Graph
```
POST /graph/search
Content-Type: application/json

{
  "query": "machine learning",
  "limit": 10
}
```

#### Get Communities
```
GET /graph/communities
```

#### Get Insights
```
GET /graph/insights
```

#### Get Node Neighbors
```
GET /graph/neighbors/{node_id}?hops=1
```

### Search

#### Semantic Search
```
POST /search
Content-Type: application/json

{
  "query": "neural networks",
  "limit": 20,
  "filters": {}
}
```

#### Citation Search
```
POST /search/citations
Content-Type: application/json

{
  "paper_id": "uuid",
  "limit": 20
}
```

#### Author Search
```
POST /search/authors
Content-Type: application/json

{
  "author_name": "John Doe",
  "limit": 20
}
```

#### Advanced Search
```
POST /search/advanced
Content-Type: application/json

{
  "query": "machine learning",
  "filters": {
    "year_from": 2020,
    "year_to": 2024,
    "keywords": ["AI", "ML"]
  },
  "limit": 20
}
```

### Trends

#### Get Trends
```
GET /trends?years=5
```

#### Get Topic Trends
```
GET /trends/topics?years=5&limit=10
```

#### Get Methodology Trends
```
GET /trends/methods?years=5&limit=10
```

#### Get Timeline
```
GET /trends/timeline
```

#### Get Emerging Topics
```
GET /trends/emerging?limit=10
```

## Rate Limiting

(To be implemented)
- Default: 100 requests per minute
- Headers: `X-RateLimit-*`

## Pagination

Use `skip` and `limit` parameters:
```
GET /papers?skip=0&limit=20
```

## Filtering

Supported filters vary by endpoint. Check specific endpoint documentation.

## Sorting

(To be implemented)

## Examples

### cURL
```bash
# List papers
curl http://localhost:8000/api/papers

# Search
curl -X POST http://localhost:8000/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "AI", "limit": 10}'
```

### JavaScript/Fetch
```javascript
// List papers
const response = await fetch('http://localhost:8000/api/papers')
const data = await response.json()

// Search
const result = await fetch('http://localhost:8000/api/search', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query: 'AI', limit: 10 })
})
```

### Python
```python
import requests

# List papers
response = requests.get('http://localhost:8000/api/papers')
data = response.json()

# Search
result = requests.post('http://localhost:8000/api/search', json={
    'query': 'AI',
    'limit': 10
})
```

## Webhooks

(To be implemented)

## WebSocket

(To be implemented)

---

For more information, see [README.md](../README.md)
