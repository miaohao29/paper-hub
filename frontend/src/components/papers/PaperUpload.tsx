import { useState } from 'react'
import { usePapers } from '@/hooks/usePapers'
import { LoadingSpinner } from '@/components/common/LoadingSpinner'
import toast from 'react-hot-toast'
import { Upload, Link as LinkIcon } from 'lucide-react'

export const PaperUpload = ({ onClose }: { onClose: () => void }) => {
  const { uploadPaper, importFromArxiv } = usePapers()
  const [arxivId, setArxivId] = useState('')
  const [loading, setLoading] = useState(false)

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    setLoading(true)
    try {
      await uploadPaper(file)
      onClose()
    } catch (error) {
      toast.error('Upload failed')
    } finally {
      setLoading(false)
    }
  }

  const handleArxivImport = async () => {
    if (!arxivId.trim()) {
      toast.error('Please enter an arXiv ID')
      return
    }

    setLoading(true)
    try {
      await importFromArxiv(arxivId)
      setArxivId('')
      onClose()
    } catch (error) {
      toast.error('Import failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="bg-card border border-border rounded-lg p-6 space-y-4">
      <h3 className="text-lg font-semibold">Add Paper</h3>

      <div className="space-y-4">
        {/* File Upload */}
        <div>
          <label className="flex items-center justify-center border-2 border-dashed border-border rounded-lg p-6 cursor-pointer hover:border-primary transition-colors">
            <div className="flex flex-col items-center gap-2">
              <Upload size={20} className="text-muted-foreground" />
              <span className="text-sm">Upload PDF or DOCX</span>
            </div>
            <input
              type="file"
              accept=".pdf,.docx"
              onChange={handleFileUpload}
              className="hidden"
              disabled={loading}
            />
          </label>
        </div>

        <div className="relative">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t border-border"></div>
          </div>
          <div className="relative flex justify-center text-sm">
            <span className="px-2 bg-card text-muted-foreground">or</span>
          </div>
        </div>

        {/* arXiv Import */}
        <div className="flex gap-2">
          <div className="flex-1">
            <div className="flex items-center gap-2 px-3 py-2 border border-border rounded-lg">
              <LinkIcon size={16} className="text-muted-foreground" />
              <input
                type="text"
                placeholder="Enter arXiv ID (e.g., 2301.00001)"
                value={arxivId}
                onChange={(e) => setArxivId(e.target.value)}
                className="flex-1 outline-none bg-transparent"
                disabled={loading}
              />
            </div>
          </div>
          <button
            onClick={handleArxivImport}
            disabled={loading}
            className="px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 disabled:opacity-50 flex items-center gap-2"
          >
            {loading ? <LoadingSpinner size="sm" /> : 'Import'}
          </button>
        </div>
      </div>
    </div>
  )
}
