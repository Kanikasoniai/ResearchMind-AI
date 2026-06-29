import { useState } from "react";
import { Send } from "lucide-react";

type Props = {
  onSend: (message: string) => void;
};

export default function ChatInput({ onSend }: Props) {
  const [message, setMessage] = useState("");

  function submit(e: React.FormEvent) {
    e.preventDefault();

    if (!message.trim()) return;

    onSend(message);
    setMessage("");
  }

  return (
    <form
      onSubmit={submit}
      className="border-t border-slate-800 p-4"
    >
      <div className="flex rounded-xl bg-slate-800">

        <input
          className="flex-1 bg-transparent px-5 py-4 outline-none text-white"
          placeholder="Ask anything about your research paper..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />

        <button
          className="px-6 text-blue-400 hover:text-blue-300"
        >
          <Send />
        </button>

      </div>
    </form>
  );
}