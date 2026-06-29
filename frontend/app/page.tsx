"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import LanguageSelector from "@/components/LanguageSelector";

export default function HomePage() {
  const [language, setLanguage] = useState("en");
  const router = useRouter();

  const handleContinue = () => {
    // Later we will save the selected language
    // in local storage and send it to the backend.
    router.push("/login");
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-green-100 flex items-center justify-center px-6">

      <div className="bg-white rounded-3xl shadow-2xl p-10 w-full max-w-lg">

        <h1 className="text-5xl font-bold text-center text-blue-700">
          🇮🇳 Bharat Sahayak AI
        </h1>

        <p className="text-center text-gray-600 mt-4 mb-8 text-lg">
          AI Powered Multilingual Government Scheme Assistant
        </p>

        <label className="block mb-3 font-semibold text-gray-700">
          🌐 Select Preferred Language
        </label>

        <LanguageSelector
          value={language}
          onChange={setLanguage}
        />

        <div className="mt-5 text-center text-gray-600">
          Selected Language:
          <span className="ml-2 font-bold text-blue-700">
            {language.toUpperCase()}
          </span>
        </div>

        <button
          onClick={handleContinue}
          className="mt-8 w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-xl text-lg font-semibold transition duration-300"
        >
          Continue
        </button>

      </div>

    </main>
  );
}