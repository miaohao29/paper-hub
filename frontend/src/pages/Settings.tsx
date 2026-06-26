const Settings = () => {
  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Settings</h1>
      <div className="max-w-2xl space-y-6">
        <div className="bg-card border border-border rounded-lg p-6">
          <h2 className="text-lg font-bold mb-4">API Configuration</h2>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2">API URL</label>
              <input
                type="text"
                defaultValue="http://localhost:8000"
                className="w-full px-3 py-2 border border-border rounded-lg bg-background"
              />
            </div>
          </div>
        </div>

        <div className="bg-card border border-border rounded-lg p-6">
          <h2 className="text-lg font-bold mb-4">Preferences</h2>
          <div className="space-y-4">
            <label className="flex items-center gap-2">
              <input type="checkbox" className="w-4 h-4" defaultChecked />
              <span>Dark Mode</span>
            </label>
            <label className="flex items-center gap-2">
              <input type="checkbox" className="w-4 h-4" defaultChecked />
              <span>Enable Notifications</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Settings
