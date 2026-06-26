import { create } from 'zustand'
import { GraphNode, GraphEdge } from '@/types/graph'

interface GraphStore {
  nodes: GraphNode[]
  edges: GraphEdge[]
  loading: boolean
  selectedNode: GraphNode | null
  setNodes: (nodes: GraphNode[]) => void
  setEdges: (edges: GraphEdge[]) => void
  setLoading: (loading: boolean) => void
  setSelectedNode: (node: GraphNode | null) => void
  updateGraph: (nodes: GraphNode[], edges: GraphEdge[]) => void
}

export const useGraphStore = create<GraphStore>((set) => ({
  nodes: [],
  edges: [],
  loading: false,
  selectedNode: null,
  setNodes: (nodes) => set({ nodes }),
  setEdges: (edges) => set({ edges }),
  setLoading: (loading) => set({ loading }),
  setSelectedNode: (selectedNode) => set({ selectedNode }),
  updateGraph: (nodes, edges) => set({ nodes, edges }),
}))
