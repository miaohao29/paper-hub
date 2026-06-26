import { Link, useLocation } from 'react-router-dom'
import {
  BookOpen,
  Network,
  TrendingUp,
  Search,
  Settings,
  Home,
  BarChart3,
} from 'lucide-react'
import { useUIStore } from '@/stores/uiStore'

const menuItems = [
  { icon: Home, label: 'Dashboard', path: '/' },
  { icon: BookOpen, label: 'Papers', path: '/papers' },
  { icon: Network, label: 'Knowledge Graph', path: '/graph' },
  { icon: BarChart3, label: 'Analysis', path: '/analysis' },
  { icon: TrendingUp, label: 'Trends', path: '/trends' },
  { icon: Search, label: 'Search', path: '/search' },
  { icon: Settings, label: 'Settings', path: '/settings' },
]

export const Sidebar = () => {
  const location = useLocation()
  const { sidebarOpen } = useUIStore()

  return (
    <aside
      className={`${
        sidebarOpen ? 'w-64' : 'w-20'
      } bg-card border-r border-border transition-all duration-300 flex flex-col`}
    >
      <div className="p-4 border-b border-border">
        <h2 className={`font-bold ${sidebarOpen ? 'text-xl' : 'text-lg text-center'}`}>
          {sidebarOpen ? 'PH' : '📄'}
        </h2>
      </div>
      <nav className="flex-1 overflow-y-auto p-4 space-y-2">
        {menuItems.map((item) => {
          const Icon = item.icon
          const isActive = location.pathname === item.path
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`flex items-center gap-3 px-4 py-2 rounded-lg transition-colors ${
                isActive
                  ? 'bg-primary text-primary-foreground'
                  : 'hover:bg-muted text-foreground'
              }`}
            >
              <Icon size={20} className="flex-shrink-0" />
              {sidebarOpen && <span>{item.label}</span>}
            </Link>
          )
        })}
      </nav>
    </aside>
  )
}
