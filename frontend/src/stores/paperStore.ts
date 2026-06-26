import { create } from 'zustand'
import { Paper } from '@/types/paper'

interface PaperStore {
  papers: Paper[]
  loading: boolean
  error: string | null
  selectedPaper: Paper | null
  setPapers: (papers: Paper[]) => void
  setLoading: (loading: boolean) => void
  setError: (error: string | null) => void
  setSelectedPaper: (paper: Paper | null) => void
  addPaper: (paper: Paper) => void
  removePaper: (id: string) => void
  updatePaper: (id: string, paper: Partial<Paper>) => void
}

export const usePaperStore = create<PaperStore>((set) => ({
  papers: [],
  loading: false,
  error: null,
  selectedPaper: null,
  setPapers: (papers) => set({ papers }),
  setLoading: (loading) => set({ loading }),
  setError: (error) => set({ error }),
  setSelectedPaper: (selectedPaper) => set({ selectedPaper }),
  addPaper: (paper) => set((state) => ({ papers: [paper, ...state.papers] })),
  removePaper: (id) =>
    set((state) => ({
      papers: state.papers.filter((p) => p.id !== id),
    })),
  updatePaper: (id, paper) =>
    set((state) => ({
      papers: state.papers.map((p) => (p.id === id ? { ...p, ...paper } : p)),
    })),
}))
