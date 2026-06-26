import { useState, useEffect } from 'react'
import { useGraphStore } from '@/stores/graphStore'
import { graphApi } from '@/services/api'
import toast from 'react-hot-toast'

export const useGraph = () => {
  const { nodes, edges, loading, selectedNode, setNodes, setEdges, setLoading, setSelectedNode } =
    useGraphStore()
  const [insights, setInsights] = useState(null)

  const fetchGraph = async () => {
    setLoading(true)
    try {
      const [nodesResponse, edgesResponse] = await Promise.all([
        graphApi.getNodes(),
        graphApi.getEdges(),
      ])
      setNodes(nodesResponse.data.nodes)
      setEdges(edgesResponse.data.edges)
    } catch (err) {
      toast.error('Failed to fetch graph')
    } finally {
      setLoading(false)
    }
  }

  const fetchInsights = async () => {
    try {
      const response = await graphApi.getInsights()
      setInsights(response.data)
    } catch (err) {
      toast.error('Failed to fetch insights')
    }
  }

  const searchGraph = async (query: string) => {
    try {
      const response = await graphApi.searchGraph(query)
      return response.data.results
    } catch (err) {
      toast.error('Search failed')
      return []
    }
  }

  return {
    nodes,
    edges,
    loading,
    selectedNode,
    insights,
    setSelectedNode,
    fetchGraph,
    fetchInsights,
    searchGraph,
  }
}
