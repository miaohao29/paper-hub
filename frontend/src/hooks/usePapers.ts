import { useState, useEffect } from 'react'
import { usePaperStore } from '@/stores/paperStore'
import { paperApi } from '@/services/api'
import toast from 'react-hot-toast'

export const usePapers = () => {
  const { papers, loading, error, setPapers, setLoading, setError } = usePaperStore()
  const [total, setTotal] = useState(0)

  const fetchPapers = async (skip = 0, limit = 20, search?: string) => {
    setLoading(true)
    try {
      const response = await paperApi.listPapers(skip, limit, search)
      setPapers(response.data.papers)
      setTotal(response.data.total)
      setError(null)
    } catch (err: any) {
      setError(err.message)
      toast.error('Failed to fetch papers')
    } finally {
      setLoading(false)
    }
  }

  const uploadPaper = async (file: File) => {
    try {
      const response = await paperApi.uploadPaper(file)
      setPapers([response.data, ...papers])
      toast.success('Paper uploaded successfully')
      return response.data
    } catch (err: any) {
      toast.error('Failed to upload paper')
      throw err
    }
  }

  const importFromArxiv = async (arxiv_id: string) => {
    try {
      const response = await paperApi.importFromArxiv(arxiv_id)
      setPapers([response.data, ...papers])
      toast.success('Paper imported from arXiv')
      return response.data
    } catch (err: any) {
      toast.error('Failed to import from arXiv')
      throw err
    }
  }

  return {
    papers,
    loading,
    error,
    total,
    fetchPapers,
    uploadPaper,
    importFromArxiv,
  }
}
