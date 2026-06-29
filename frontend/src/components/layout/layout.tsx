type LayoutProps = {
  sidebar: React.ReactNode;
  children: React.ReactNode;
};

export default function Layout({
  sidebar,
  children,
}: LayoutProps) {
  return (
    <div className="flex h-screen bg-slate-950 text-white">
      <aside className="w-72 border-r border-slate-800">
        {sidebar}
      </aside>

      <main className="flex-1 overflow-auto">
        {children}
      </main>
    </div>
  );
}