import {
  Upload,
  MessageSquare,
  FileText,
  NotebookPen,
  BookOpen,
  Settings,
} from "lucide-react";

const menu = [
  { icon: Upload, label: "Upload Paper" },
  { icon: MessageSquare, label: "AI Chat" },
  { icon: FileText, label: "Summary" },
  { icon: NotebookPen, label: "Notes" },
  { icon: BookOpen, label: "Flashcards" },
  { icon: Settings, label: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="h-screen w-72 bg-slate-950 border-r border-slate-800 flex flex-col">

      <div className="p-6 border-b border-slate-800">

        <h1 className="text-2xl font-bold text-white">
          🔬 ResearchMind AI
        </h1>

      </div>

      <nav className="flex-1 p-4 space-y-2">

        {menu.map((item) => {

          const Icon = item.icon;

          return (
            <button
              key={item.label}
              className="flex w-full items-center gap-3 rounded-lg px-4 py-3 text-slate-300 hover:bg-slate-800 hover:text-white transition"
            >
              <Icon size={20} />
              {item.label}
            </button>
          );

        })}

      </nav>

    </aside>
  );
}