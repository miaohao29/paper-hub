const Dashboard = () => {
  return (
    <div className="p-6 space-y-6">
      <div>
        <h1 className="text-3xl font-bold mb-2">Welcome to Paper Hub</h1>
        <p className="text-muted-foreground">Your academic knowledge base for research papers</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-card border border-border rounded-lg p-6">
          <h3 className="text-sm font-medium text-muted-foreground mb-2">Total Papers</h3>
          <div className="text-3xl font-bold">0</div>
        </div>
        <div className="bg-card border border-border rounded-lg p-6">
          <h3 className="text-sm font-medium text-muted-foreground mb-2">Authors</h3>
          <div className="text-3xl font-bold">0</div>
        </div>
        <div className="bg-card border border-border rounded-lg p-6">
          <h3 className="text-sm font-medium text-muted-foreground mb-2">Topics</h3>
          <div className="text-3xl font-bold">0</div>
        </div>
        <div className="bg-card border border-border rounded-lg p-6">
          <h3 className="text-sm font-medium text-muted-foreground mb-2">Insights</h3>
          <div className="text-3xl font-bold">0</div>
        </div>
      </div>

      <div className="bg-card border border-border rounded-lg p-6">
        <h2 className="text-xl font-bold mb-4">Getting Started</h2>
        <ul className="space-y-2 text-sm text-muted-foreground">
          <li>✓ Upload your first paper</li>
          <li>✓ Import papers from arXiv</li>
          <li>✓ Explore the knowledge graph</li>
          <li>✓ Analyze research trends</li>
          <li>✓ Discover innovation points</li>
        </ul>
      </div>
    </div>
  )
}

export default Dashboard
