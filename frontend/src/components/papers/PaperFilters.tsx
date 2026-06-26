import { useState } from 'react'
import { Search } from 'lucide-react'

export const PaperFilters = ({ onSearch }: { onSearch: (query: string) => void }) => {
  const [query, setQuery] = useState('')

  const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value
    setQuery(value)
    onSearch(value)
  }

  return (
    <div className="flex items-center gap-2 px-3 py-2 bg-card border border-border rounded-lg">
      <Search size={20} className="text-muted-foreground" />
      <input
        type="text"
        placeholder="Search papers..."
        value={query}
        onChange={handleSearch}
        className="flex-1 outline-none bg-transparent"
      />
    </div>
  )
}
