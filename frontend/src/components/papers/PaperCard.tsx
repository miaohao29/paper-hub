import { Link } from 'react-router-dom'
import { Paper } from '@/types/paper'
import { formatDate } from '@/utils/date'
import { FileText, Users, Zap } from 'lucide-react'

export const PaperCard = ({ paper }: { paper: Paper }) => {
  return (
    <Link to={`/papers/${paper.id}`}>
      <div className="bg-card border border-border rounded-lg p-4 hover:shadow-lg transition-shadow cursor-pointer">
        <div className="flex items-start gap-3 mb-3">
          <FileText className="text-primary flex-shrink-0 mt-1" size={20} />
          <h3 className="font-semibold line-clamp-2">{paper.title}</h3>
        </div>

        <p className="text-sm text-muted-foreground line-clamp-2 mb-3">
          {paper.abstract}
        </p>

        <div className="space-y-2 text-sm">
          {paper.authors.length > 0 && (
            <div className="flex items-center gap-2 text-muted-foreground">
              <Users size={16} />
              <span>{paper.authors.map((a) => a.name).join(', ')}</span>
            </div>
          )}

          {paper.publication_year && (
            <div className="text-muted-foreground">
              {paper.publication_year} {paper.venue && `• ${paper.venue}`}
            </div>
          )}
        </div>

        {paper.keywords.length > 0 && (
          <div className="mt-3 flex flex-wrap gap-1">
            {paper.keywords.slice(0, 3).map((kw) => (
              <span
                key={kw.id}
                className="text-xs bg-accent/10 text-accent px-2 py-1 rounded"
              >
                {kw.keyword}
              </span>
            ))}
          </div>
        )}
      </div>
    </Link>
  )
}
