import { useParams } from 'react-router-dom'
import { useState, useEffect } from 'react'
import { paperApi } from '@/services/api'
import { Paper as PaperType } from '@/types/paper'
import { PaperDetail } from '@/components/papers/PaperDetailView'
import { InnovationPoints } from '@/components/analysis/InnovationPoints'
import { LoadingSpinner } from '@/components/common/LoadingSpinner'
import toast from 'react-hot-toast'

const PaperDetail = () => {
  const { id } = useParams<{ id: string }>()
  const [paper, setPaper] = useState<PaperType | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchPaper = async () => {
      if (!id) return
      try {
        const response = await paperApi.getPaper(id)
        setPaper(response.data)
      } catch (error) {
        toast.error('Failed to fetch paper')
      } finally {
        setLoading(false)
      }
    }

    fetchPaper()
  }, [id])

  if (loading) {
    return (
      <div className="flex justify-center items-center h-96">
        <LoadingSpinner />
      </div>
    )
  }

  if (!paper) {
    return <div className="p-6 text-center text-muted-foreground">Paper not found</div>
  }

  return (
    <div className="p-6 space-y-8">
      <PaperDetail paper={paper} />
      <InnovationPoints paperId={id!} />
    </div>
  )
}

export default PaperDetail
