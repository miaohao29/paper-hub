export type Trend = {
  id: string
  trend_name: string
  trend_type: 'topic' | 'methodology' | 'tool'
  start_year?: number
  end_year?: number
  growth_rate?: number
  paper_count?: number
  description?: string
}

export type TimelineData = {
  year: number
  count: number
}
