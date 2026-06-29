"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export default function Navbar() {
  const pathname = usePathname();

  const navItems = [
    { name: "🏠 Home", href: "/" },
    { name: "📊 Dashboard", href: "/dashboard" },
    { name: "📋 Eligibility", href: "/eligibility" },
    { name: "🏛️ Schemes", href: "/results" },
    { name: "🤖 AI Assistant", href: "/chat" },
  ];

  return (
    <header className="sticky top-0 z-50 bg-gradient-to-r from-blue-700 via-blue-600 to-indigo-700 shadow-xl">

      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">

        {/* Logo */}

        <Link href="/" className="flex items-center gap-3">

          <div className="text-4xl">
            🇮🇳
          </div>

          <div>

            <h1 className="text-2xl font-bold text-white">
              Bharat Sahayak AI
            </h1>

            <p className="text-xs text-blue-100">
              AI Powered Government Scheme Assistant
            </p>

          </div>

        </Link>

        {/* Navigation */}

        <nav className="hidden lg:flex gap-6">

          {navItems.map((item) => (

            <Link
              key={item.href}
              href={item.href}
              className={`font-medium transition-all duration-300 px-3 py-2 rounded-lg ${
                pathname === item.href
                  ? "bg-white text-blue-700"
                  : "text-white hover:bg-blue-500"
              }`}
            >
              {item.name}
            </Link>

          ))}

        </nav>

        {/* Right Buttons */}

        <div className="flex gap-3">

          <Link href="/login">

            <button className="bg-white text-blue-700 px-5 py-2 rounded-lg font-semibold hover:bg-gray-100 transition">
              Login
            </button>

          </Link>

          <Link href="/register">

            <button className="bg-green-500 text-white px-5 py-2 rounded-lg font-semibold hover:bg-green-600 transition">
              Register
            </button>

          </Link>

        </div>

      </div>

      {/* Mobile Navigation */}

      <div className="lg:hidden bg-blue-800 px-3 py-3 overflow-x-auto whitespace-nowrap">

        <div className="flex gap-3">

          {navItems.map((item) => (

            <Link
              key={item.href}
              href={item.href}
              className={`px-4 py-2 rounded-lg text-sm ${
                pathname === item.href
                  ? "bg-white text-blue-700"
                  : "bg-blue-600 text-white"
              }`}
            >
              {item.name}
            </Link>

          ))}

        </div>

      </div>

    </header>
  );
}