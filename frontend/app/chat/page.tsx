"use client";

import { useState } from "react";

export default function ChatPage() {
  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([
    {
      sender: "assistant",
      text: "🙏 Namaste! I am Bharat Sahayak AI. Ask me about any Government Scheme.",
    },
  ]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = {
      sender: "user",
      text: message,
    };

    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await fetch("http://localhost:8000/ai/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message,
        }),
      });

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          text: data.response,
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          text: "Unable to connect to AI service.",
        },
      ]);
    }

    setMessage("");
  };

  return (
    <main className="min-h-screen bg-gray-100 flex flex-col">

      {/* Header */}

      <div className="bg-blue-700 text-white p-5 shadow-lg">

        <h1 className="text-3xl font-bold">
          🤖 Bharat Sahayak AI
        </h1>

        <p>
          Multilingual Government Scheme Assistant
        </p>

      </div>

      {/* Chat */}

      <div className="flex-1 overflow-y-auto p-8">

        {messages.map((msg, index) => (

          <div
            key={index}
            className={`mb-5 flex ${
              msg.sender === "user"
                ? "justify-end"
                : "justify-start"
            }`}
          >

            <div
              className={`max-w-xl rounded-2xl px-5 py-4 ${
                msg.sender === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-white shadow"
              }`}
            >

              {msg.text}

            </div>

          </div>

        ))}

      </div>

      {/* Input */}

      <div className="bg-white p-5 shadow-inner">

        <div className="flex gap-3">

          <input
            className="flex-1 border rounded-xl p-4"
            placeholder="Ask about Government Schemes..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />

          <button
            onClick={sendMessage}
            className="bg-blue-700 text-white px-8 rounded-xl"
          >
            Send
          </button>

          <button
            className="bg-green-600 text-white px-6 rounded-xl"
          >
            🎤
          </button>

        </div>

      </div>

    </main>
  );
}