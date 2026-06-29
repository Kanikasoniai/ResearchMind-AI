import UploadCard from "../components/upload/UploadCard";
import ChatWindow from "../components/chat/ChatWindow";

export default function Home() {
  return (
    <div className="grid grid-cols-3 h-full">

      <div className="border-r border-slate-800 p-6">
        <UploadCard />
      </div>

      <div className="col-span-2">
        <ChatWindow />
      </div>

    </div>
  );
}