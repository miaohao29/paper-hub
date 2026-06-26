import { useState, useEffect } from 'react'
import { useSearch } from '@/hooks/useSearch'
import { LoadingSpinner } from '@/components/common/LoadingSpinner'
import { Search as SearchIcon } from 'lucide-react'

export const SearchInterface = () => {
  const { results, loading, search } = useSearch()
  const [query, setQuery] = useState('')

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    search(query)
  }

  return (
    <div className="space-y-4">
      <form onSubmit={handleSearch} className="flex gap-2">
        <div className="flex-1 flex items-center gap-2 px-3 py-2 bg-card border border-border rounded-lg">
          <SearchIcon size={20} className="text-muted-foreground" />
          <input
            type="text"
            placeholder="Search papers, authors, keywords..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="flex-1 outline-none bg-transparent"
          />
        </div>
        <button
          type="submit"
          className="px-6 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90"
        >
          Search
        </button>
      </form>

      {loading ? (
        <div className="flex justify-center py-12">
          <LoadingSpinner />
        </div>
      ) : results.length > 0 ? (
        <div className="space-y-3">
          {results.map((result, idx) => (
            <div key={idx} className="bg-card border border-border rounded-lg p-4 hover:shadow-lg transition-shadow">
              <h3 className="font-semibold mb-1">{result.title}</h3>
              <p className="text-sm text-muted-foreground mb-2 line-clamp-2">
                {result.abstract}
              </p>
              <div className="flex items-center justify-between text-sm">
                <span className="text-muted-foreground">
                  {result.authors?.join(', ')}
                </span>
                <span className="text-accent font-medium">
                  {(result.relevance_score * 100).toFixed(0)}% match
                </span>
              </div>
            </div>
          ))}
        </div>
      ) : null}
    </div>
  )
}
