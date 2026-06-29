"use client";

import Link from "next/link";

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-green-100">

      {/* Header */}

      <header className="bg-blue-700 text-white shadow-lg">

        <div className="max-w-7xl mx-auto flex justify-between items-center px-8 py-5">

          <div>
            <h1 className="text-3xl font-bold">
              🇮🇳 Bharat Sahayak AI
            </h1>

            <p className="text-sm opacity-90">
              AI Powered Government Scheme Assistant
            </p>
          </div>

          <button className="bg-white text-blue-700 px-5 py-2 rounded-lg font-semibold hover:bg-gray-100">
            Logout
          </button>

        </div>

      </header>

      {/* Welcome */}

      <section className="max-w-7xl mx-auto mt-10 px-6">

        <h2 className="text-4xl font-bold text-blue-800">
          Welcome 👋
        </h2>

        <p className="text-gray-600 mt-3 text-lg">
          Find the best Government Schemes based on your profile using Artificial Intelligence.
        </p>

      </section>

      {/* Dashboard Cards */}

      <section className="max-w-7xl mx-auto mt-12 px-6">

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">

          {/* Eligibility */}

          <Link href="/eligibility">

            <div className="bg-white rounded-3xl shadow-xl p-8 hover:shadow-2xl cursor-pointer transition">

              <div className="text-5xl">
                📋
              </div>

              <h3 className="text-2xl font-bold mt-5">
                Check Eligibility
              </h3>

              <p className="text-gray-600 mt-3">
                Fill your profile and instantly check all matching Government schemes.
              </p>

            </div>

          </Link>

          {/* AI Chat */}

          <Link href="/chat">

            <div className="bg-white rounded-3xl shadow-xl p-8 hover:shadow-2xl cursor-pointer transition">

              <div className="text-5xl">
                🤖
              </div>

              <h3 className="text-2xl font-bold mt-5">
                AI Assistant
              </h3>

              <p className="text-gray-600 mt-3">
                Ask questions in your preferred language and receive AI-powered guidance.
              </p>

            </div>

          </Link>

          {/* Schemes */}

          <Link href="/results">

            <div className="bg-white rounded-3xl shadow-xl p-8 hover:shadow-2xl cursor-pointer transition">

              <div className="text-5xl">
                🏛️
              </div>

              <h3 className="text-2xl font-bold mt-5">
                Government Schemes
              </h3>

              <p className="text-gray-600 mt-3">
                Browse all Central and State Government welfare schemes.
              </p>

            </div>

          </Link>

          {/* Saved */}

          <div className="bg-white rounded-3xl shadow-xl p-8">

            <div className="text-5xl">
              ❤️
            </div>

            <h3 className="text-2xl font-bold mt-5">
              Saved Schemes
            </h3>

            <p className="text-gray-600 mt-3">
              View all your bookmarked schemes in one place.
            </p>

          </div>

          {/* Documents */}

          <div className="bg-white rounded-3xl shadow-xl p-8">

            <div className="text-5xl">
              📄
            </div>

            <h3 className="text-2xl font-bold mt-5">
              Documents
            </h3>

            <p className="text-gray-600 mt-3">
              Upload and manage your Aadhaar, Income Certificate, Caste Certificate and more.
            </p>

          </div>

          {/* Profile */}

          <div className="bg-white rounded-3xl shadow-xl p-8">

            <div className="text-5xl">
              👤
            </div>

            <h3 className="text-2xl font-bold mt-5">
              My Profile
            </h3>

            <p className="text-gray-600 mt-3">
              Update your personal information and eligibility profile.
            </p>

          </div>

        </div>

      </section>

    </main>
  );
}