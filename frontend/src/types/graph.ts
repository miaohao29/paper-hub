export type GraphNode = {
  id: string
  label: string
  type: 'paper' | 'author' | 'concept' | 'methodology'
  description?: string
  metadata?: any
}

export type GraphEdge = {
  source: string
  target: string
  type: string
  weight?: number
}

export type Community = {
  id: string
  members: string[]
  cohesion: number
}
