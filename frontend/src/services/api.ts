import axios from 'axios'
import { Paper, Innovation, Analysis } from '@/types/paper'
import { GraphNode, GraphEdge } from '@/types/graph'
import { Trend } from '@/types/trend'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const client = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Paper endpoints
export const paperApi = {
  listPapers: (skip = 0, limit = 20, search?: string) =>
    client.get<{ papers: Paper[]; total: number }>('/papers', {
      params: { skip, limit, search },
    }),

  getPaper: (id: string) => client.get<Paper>(`/papers/${id}`),

  createPaper: (data: any) => client.post<Paper>('/papers', data),

  uploadPaper: (file: File) => {
    const formData = new FormData()
    formData.append('file', file)
    return client.post<Paper>('/papers/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
  },

  updatePaper: (id: string, data: any) =>
    client.put<Paper>(`/papers/${id}`, data),

  deletePaper: (id: string) => client.delete(`/papers/${id}`),

  importFromArxiv: (arxiv_id: string) =>
    client.post<Paper>('/papers/arxiv/import', { arxiv_id }),
}

// Analysis endpoints
export const analysisApi = {
  analyzePaper: (paper_id: string) =>
    client.post(`/analysis/${paper_id}/analyze`),

  getInnovations: (paper_id: string) =>
    client.get<{ innovations: Innovation[] }>(
      `/analysis/${paper_id}/innovations`
    ),

  getRelationships: (paper_id: string) =>
    client.get(`/analysis/${paper_id}/relationships`),

  comparePapers: (paper_ids: string[]) =>
    client.post('/analysis/compare', { paper_ids }),
}

// Graph endpoints
export const graphApi = {
  getNodes: (node_type?: string) =>
    client.get<{ nodes: GraphNode[] }>('/graph/nodes', {
      params: { node_type },
    }),

  getEdges: () => client.get<{ edges: GraphEdge[] }>('/graph/edges'),

  searchGraph: (query: string, limit = 10) =>
    client.post('/graph/search', { query, limit }),

  getCommunities: () => client.get('/graph/communities'),

  getInsights: () => client.get('/graph/insights'),

  getNeighbors: (node_id: string, hops = 1) =>
    client.get(`/graph/neighbors/${node_id}`, { params: { hops } }),
}

// Search endpoints
export const searchApi = {
  semanticSearch: (query: string, limit = 20, filters?: any) =>
    client.post('/search', { query, limit, filters }),

  citationSearch: (paper_id: string, limit = 20) =>
    client.post('/search/citations', { paper_id, limit }),

  authorSearch: (author_name: string, limit = 20) =>
    client.post('/search/authors', { author_name, limit }),

  advancedSearch: (query: string, filters: any, limit = 20) =>
    client.post('/search/advanced', { query, filters, limit }),
}

// Trends endpoints
export const trendsApi = {
  getTrends: (years = 5) => client.get<{ trends: any }>('/trends', { params: { years } }),

  getTopicTrends: (years = 5, limit = 10) =>
    client.get<{ topics: any[] }>('/trends/topics', {
      params: { years, limit },
    }),

  getMethodologyTrends: (years = 5, limit = 10) =>
    client.get('/trends/methods', { params: { years, limit } }),

  getTimeline: () => client.get('/trends/timeline'),

  getEmergingTopics: (limit = 10) =>
    client.get('/trends/emerging', { params: { limit } }),
}

export default client
