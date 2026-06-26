import '../styles/globals.css'
import { Toaster } from 'react-hot-toast'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Header } from '@/components/common/Header'
import { Sidebar } from '@/components/common/Sidebar'
import Dashboard from '@/pages/Dashboard'
import Papers from '@/pages/Papers'
import PaperDetail from '@/pages/PaperDetail'
import Graph from '@/pages/Graph'
import Analysis from '@/pages/Analysis'
import Trends from '@/pages/Trends'
import Search from '@/pages/Search'
import Settings from '@/pages/Settings'

function App() {
  return (
    <Router>
      <div className="flex h-screen bg-background">
        <Sidebar />
        <div className="flex-1 flex flex-col overflow-hidden">
          <Header />
          <main className="flex-1 overflow-auto">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/papers" element={<Papers />} />
              <Route path="/papers/:id" element={<PaperDetail />} />
              <Route path="/graph" element={<Graph />} />
              <Route path="/analysis" element={<Analysis />} />
              <Route path="/trends" element={<Trends />} />
              <Route path="/search" element={<Search />} />
              <Route path="/settings" element={<Settings />} />
            </Routes>
          </main>
        </div>
        <Toaster position="bottom-right" />
      </div>
    </Router>
  )
}

export default App
