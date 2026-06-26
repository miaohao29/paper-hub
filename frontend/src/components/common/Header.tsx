import { Link } from 'react-router-dom'
import { Menu, X, Search, Settings } from 'lucide-react'
import { useUIStore } from '@/stores/uiStore'

export const Header = () => {
  const { sidebarOpen, toggleSidebar } = useUIStore()

  return (
    <header className="bg-white border-b border-border">
      <div className="flex items-center justify-between px-6 py-4">
        <button
          onClick={toggleSidebar}
          className="p-2 hover:bg-muted rounded-lg"
        >
          {sidebarOpen ? <X size={20} /> : <Menu size={20} />}
        </button>
        <h1 className="text-xl font-semibold flex-1 ml-4">Paper Hub</h1>
        <div className="flex items-center gap-4">
          <Link to="/search" className="p-2 hover:bg-muted rounded-lg">
            <Search size={20} />
          </Link>
          <Link to="/settings" className="p-2 hover:bg-muted rounded-lg">
            <Settings size={20} />
          </Link>
        </div>
      </div>
    </header>
  )
}
