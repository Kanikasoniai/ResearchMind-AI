type Props = {
  role: "user" | "assistant";
  text: string;
};

export default function Message({
  role,
  text,
}: Props) {
  const isUser = role === "user";

  return (
    <div
      className={`mb-6 flex ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`max-w-3xl rounded-2xl px-5 py-4 shadow-lg ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-slate-800 text-slate-100"
        }`}
      >
        {text}
      </div>
    </div>
  );
}