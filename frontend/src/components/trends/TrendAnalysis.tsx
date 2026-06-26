import { useState, useEffect } from 'react'
import { trendsApi } from '@/services/api'
import { LoadingSpinner } from '@/components/common/LoadingSpinner'
import toast from 'react-hot-toast'

export const TrendAnalysis = () => {
  const [topics, setTopics] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchTrends = async () => {
      try {
        const response = await trendsApi.getTopicTrends(5, 15)
        setTopics(response.data.topics)
      } catch (error) {
        toast.error('Failed to fetch trends')
      } finally {
        setLoading(false)
      }
    }

    fetchTrends()
  }, [])

  if (loading) {
    return (
      <div className="flex justify-center py-12">
        <LoadingSpinner />
      </div>
    )
  }

  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-bold">Research Trends</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {topics.map((topic, idx) => (
          <div key={idx} className="bg-card border border-border rounded-lg p-4">
            <div className="font-semibold mb-2">{topic.topic}</div>
            <div className="text-3xl font-bold text-primary mb-1">{topic.frequency}</div>
            <div className="text-sm text-muted-foreground">papers in this area</div>
          </div>
        ))}
      </div>
    </div>
  )
}
