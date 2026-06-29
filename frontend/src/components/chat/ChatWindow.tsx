import { useState } from "react";

import { askQuestion } from "../../api/chat";

import Message from "./Message";
import ChatInput from "./ChatInput";

type ChatMessage = {
  role: "user" | "assistant";
  text: string;
};

export default function ChatWindow() {

  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      role: "assistant",
      text: "👋 Hi! Upload a paper and ask me anything.",
    },
  ]);

  const [loading, setLoading] = useState(false);

  async function handleSend(question: string) {

    setMessages(prev => [
      ...prev,
      {
        role: "user",
        text: question,
      },
    ]);

    try {

      setLoading(true);

      const result = await askQuestion(question);

      setMessages(prev => [
        ...prev,
        {
          role: "assistant",
          text: result.answer,
        },
      ]);

    } catch (error) {

      setMessages(prev => [
        ...prev,
        {
          role: "assistant",
          text: "❌ Something went wrong.",
        },
      ]);

      console.error(error);

    } finally {

      setLoading(false);

    }

  }

  return (

    <div className="flex flex-col h-full">

      <div className="flex-1 overflow-y-auto p-6">

        {messages.map((message, index) => (

          <Message
            key={index}
            role={message.role}
            text={message.text}
          />

        ))}

        {loading && (

          <Message
            role="assistant"
            text="Thinking..."
          />

        )}

      </div>

      <ChatInput onSend={handleSend} />

    </div>

  );

}