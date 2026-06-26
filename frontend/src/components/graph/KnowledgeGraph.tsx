import { useState, useEffect } from 'react'
import { useGraph } from '@/hooks/useGraph'
import { LoadingSpinner } from '@/components/common/LoadingSpinner'
import { Sigma } from 'sigma'
import { useRef } from 'react'

export const KnowledgeGraph = () => {
  const containerRef = useRef<HTMLDivElement>(null)
  const { nodes, edges, loading, fetchGraph } = useGraph()

  useEffect(() => {
    fetchGraph()
  }, [])

  useEffect(() => {
    if (!containerRef.current || nodes.length === 0) return

    // Initialize Sigma.js graph
    // This is a placeholder - full implementation would integrate Sigma properly
    console.log('Initializing graph with', nodes.length, 'nodes and', edges.length, 'edges')
  }, [nodes, edges])

  if (loading) {
    return (
      <div className="flex justify-center items-center h-96">
        <LoadingSpinner />
      </div>
    )
  }

  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-bold">Knowledge Graph</h2>
      <div
        ref={containerRef}
        className="bg-card border border-border rounded-lg h-96 w-full"
        style={{ minHeight: '500px' }}
      >
        <div className="flex items-center justify-center h-full text-muted-foreground">
          <p>
            {nodes.length > 0
              ? `Graph ready with ${nodes.length} nodes`
              : 'No data to display'}
          </p>
        </div>
      </div>
    </div>
  )
}
