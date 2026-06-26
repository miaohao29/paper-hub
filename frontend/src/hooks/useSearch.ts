import { useState, useEffect } from 'react'
import { searchApi } from '@/services/api'
import toast from 'react-hot-toast'

export const useSearch = () => {
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(false)

  const search = async (query: string, limit = 20) => {
    if (!query.trim()) return

    setLoading(true)
    try {
      const response = await searchApi.semanticSearch(query, limit)
      setResults(response.data.results)
    } catch (err) {
      toast.error('Search failed')
    } finally {
      setLoading(false)
    }
  }

  const advancedSearch = async (query: string, filters: any) => {
    setLoading(true)
    try {
      const response = await searchApi.advancedSearch(query, filters)
      setResults(response.data.results)
    } catch (err) {
      toast.error('Advanced search failed')
    } finally {
      setLoading(false)
    }
  }

  return {
    results,
    loading,
    search,
    advancedSearch,
  }
}
