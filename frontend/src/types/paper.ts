export type Paper = {
  id: string
  title: string
  abstract?: string
  authors: Author[]
  keywords: Keyword[]
  doi?: string
  arxiv_id?: string
  publication_year?: number
  publication_date?: string
  venue?: string
  citation_count: number
  view_count: number
  processed: boolean
  created_at: string
  updated_at: string
}

export type Author = {
  id: string
  name: string
  email?: string
  affiliation?: string
  orcid?: string
}

export type Keyword = {
  id: string
  keyword: string
  category?: string
  frequency: number
}

export type Innovation = {
  id: string
  paper_id: string
  title: string
  description: string
  innovation_type: string
  significance_score?: number
}

export type Analysis = {
  id: string
  paper_id: string
  analysis_type: string
  result: any
  confidence_score?: number
}
