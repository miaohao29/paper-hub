import { useEffect, useState } from 'react'
import { analysisApi } from '@/services/api'
import { LoadingSpinner } from '@/components/common/LoadingSpinner'
import toast from 'react-hot-toast'

export const InnovationPoints = ({ paperId }: { paperId: string }) => {
  const [innovations, setInnovations] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchInnovations = async () => {
      try {
        const response = await analysisApi.getInnovations(paperId)
        setInnovations(response.data.innovations)
      } catch (error) {
        toast.error('Failed to fetch innovations')
      } finally {
        setLoading(false)
      }
    }

    fetchInnovations()
  }, [paperId])

  if (loading) {
    return (
      <div className="flex justify-center py-12">
        <LoadingSpinner />
      </div>
    )
  }

  return (
    <div className="space-y-4">
      <h2 className="text-xl font-bold">Innovation Points</h2>
      {innovations.length > 0 ? (
        <div className="space-y-3">
          {innovations.map((innovation, idx) => (
            <div key={idx} className="bg-card border border-border rounded-lg p-4">
              <h3 className="font-semibold mb-1">{innovation.title}</h3>
              <p className="text-sm text-muted-foreground mb-2">{innovation.description}</p>
              <div className="flex items-center gap-4 text-sm">
                <span className="px-2 py-1 bg-accent/10 text-accent rounded">
                  {innovation.type}
                </span>
                {innovation.significance && (
                  <span className="text-muted-foreground">
                    Significance: {(innovation.significance * 100).toFixed(0)}%
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      ) : (
        <p className="text-muted-foreground">No innovations found</p>
      )}
    </div>
  )
}
