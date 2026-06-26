import { Paper } from '@/types/paper'
import { formatDate } from '@/utils/date'
import { ExternalLink, Users, Bookmark } from 'lucide-react'

export const PaperDetail = ({ paper }: { paper: Paper }) => {
  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="space-y-2">
        <div className="flex items-start justify-between gap-4">
          <div className="flex-1">
            <h1 className="text-3xl font-bold mb-2">{paper.title}</h1>
            <div className="flex items-center gap-4 text-muted-foreground text-sm">
              {paper.doi && (
                <a
                  href={`https://doi.org/${paper.doi}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-1 hover:text-primary"
                >
                  DOI: {paper.doi}
                  <ExternalLink size={14} />
                </a>
              )}
              {paper.arxiv_id && (
                <a
                  href={`https://arxiv.org/abs/${paper.arxiv_id}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-1 hover:text-primary"
                >
                  arXiv: {paper.arxiv_id}
                  <ExternalLink size={14} />
                </a>
              )}
            </div>
          </div>
          <button className="p-2 hover:bg-muted rounded-lg">
            <Bookmark size={20} />
          </button>
        </div>
      </div>

      {/* Metadata */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {paper.publication_year && (
          <div className="bg-card border border-border rounded-lg p-3">
            <div className="text-sm text-muted-foreground">Year</div>
            <div className="font-semibold">{paper.publication_year}</div>
          </div>
        )}
        {paper.venue && (
          <div className="bg-card border border-border rounded-lg p-3">
            <div className="text-sm text-muted-foreground">Venue</div>
            <div className="font-semibold truncate">{paper.venue}</div>
          </div>
        )}
        <div className="bg-card border border-border rounded-lg p-3">
          <div className="text-sm text-muted-foreground">Citations</div>
          <div className="font-semibold">{paper.citation_count}</div>
        </div>
        <div className="bg-card border border-border rounded-lg p-3">
          <div className="text-sm text-muted-foreground">Views</div>
          <div className="font-semibold">{paper.view_count}</div>
        </div>
      </div>

      {/* Authors */}
      {paper.authors.length > 0 && (
        <div className="bg-card border border-border rounded-lg p-4">
          <div className="flex items-center gap-2 mb-3">
            <Users size={20} />
            <h2 className="text-lg font-semibold">Authors</h2>
          </div>
          <div className="space-y-2">
            {paper.authors.map((author) => (
              <div key={author.id} className="text-sm">
                <div className="font-medium">{author.name}</div>
                {author.affiliation && (
                  <div className="text-muted-foreground">{author.affiliation}</div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Abstract */}
      {paper.abstract && (
        <div className="bg-card border border-border rounded-lg p-4">
          <h2 className="text-lg font-semibold mb-3">Abstract</h2>
          <p className="text-sm leading-relaxed text-foreground">{paper.abstract}</p>
        </div>
      )}

      {/* Keywords */}
      {paper.keywords.length > 0 && (
        <div className="bg-card border border-border rounded-lg p-4">
          <h2 className="text-lg font-semibold mb-3">Keywords</h2>
          <div className="flex flex-wrap gap-2">
            {paper.keywords.map((keyword) => (
              <span
                key={keyword.id}
                className="px-3 py-1 bg-accent/10 text-accent rounded-full text-sm font-medium"
              >
                {keyword.keyword}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
