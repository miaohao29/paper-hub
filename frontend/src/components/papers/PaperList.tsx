import { useState, useEffect } from 'react'
import { usePapers } from '@/hooks/usePapers'
import { PaperCard } from './PaperCard'
import { PaperUpload } from './PaperUpload'
import { PaperFilters } from './PaperFilters'
import { LoadingSpinner } from '@/components/common/LoadingSpinner'
import { Plus } from 'lucide-react'

export const PaperList = () => {
  const { papers, loading, fetchPapers } = usePapers()
  const [showUpload, setShowUpload] = useState(false)
  const [page, setPage] = useState(0)
  const [search, setSearch] = useState('')

  useEffect(() => {
    fetchPapers(page * 20, 20, search)
  }, [page, search])

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold">Papers</h2>
        <button
          onClick={() => setShowUpload(!showUpload)}
          className="flex items-center gap-2 px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90"
        >
          <Plus size={20} />
          Add Paper
        </button>
      </div>

      {showUpload && <PaperUpload onClose={() => setShowUpload(false)} />}

      <PaperFilters onSearch={setSearch} />

      {loading ? (
        <div className="flex justify-center py-12">
          <LoadingSpinner />
        </div>
      ) : papers.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {papers.map((paper) => (
            <PaperCard key={paper.id} paper={paper} />
          ))}
        </div>
      ) : (
        <div className="text-center py-12 text-muted-foreground">
          <p>No papers found</p>
        </div>
      )}
    </div>
  )
}
