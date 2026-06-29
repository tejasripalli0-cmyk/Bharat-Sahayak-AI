import Link from "next/link";

export default function Footer() {
  return (
    <footer className="bg-slate-900 text-white mt-20">

      <div className="max-w-7xl mx-auto px-6 py-12">

        <div className="grid lg:grid-cols-4 md:grid-cols-2 gap-10">

          {/* About */}

          <div>

            <h2 className="text-2xl font-bold mb-4">
              🇮🇳 Bharat Sahayak AI
            </h2>

            <p className="text-gray-300 leading-7">
              Bharat Sahayak AI is an AI-powered multilingual Government
              Scheme Assistant that helps citizens discover Central and
              State Government welfare schemes based on their profile.
            </p>

          </div>

          {/* Quick Links */}

          <div>

            <h3 className="text-xl font-semibold mb-4">
              🚀 Quick Links
            </h3>

            <ul className="space-y-3">

              <li>
                <Link href="/" className="hover:text-yellow-300">
                  🏠 Home
                </Link>
              </li>

              <li>
                <Link href="/dashboard" className="hover:text-yellow-300">
                  📊 Dashboard
                </Link>
              </li>

              <li>
                <Link href="/eligibility" className="hover:text-yellow-300">
                  📋 Check Eligibility
                </Link>
              </li>

              <li>
                <Link href="/results" className="hover:text-yellow-300">
                  🏛 Government Schemes
                </Link>
              </li>

              <li>
                <Link href="/chat" className="hover:text-yellow-300">
                  🤖 AI Assistant
                </Link>
              </li>

            </ul>

          </div>

          {/* Support */}

          <div>

            <h3 className="text-xl font-semibold mb-4">
              📞 Support
            </h3>

            <ul className="space-y-3 text-gray-300">

              <li>
                📧 support@bharatsahayakai.in
              </li>

              <li>
                ☎ +91 1800-000-000
              </li>

              <li>
                🌐 Available in 25+ Languages
              </li>

              <li>
                🤖 AI Powered Assistance
              </li>

            </ul>

          </div>

          {/* Legal */}

          <div>

            <h3 className="text-xl font-semibold mb-4">
              🔒 Legal
            </h3>

            <ul className="space-y-3">

              <li>
                <Link href="#" className="hover:text-yellow-300">
                  Privacy Policy
                </Link>
              </li>

              <li>
                <Link href="#" className="hover:text-yellow-300">
                  Terms & Conditions
                </Link>
              </li>

              <li>
                <Link href="#" className="hover:text-yellow-300">
                  Accessibility
                </Link>
              </li>

              <li>
                <Link href="#" className="hover:text-yellow-300">
                  Contact Us
                </Link>
              </li>

            </ul>

          </div>

        </div>

        {/* Divider */}

        <div className="border-t border-gray-700 my-10"></div>

        {/* Bottom */}

        <div className="flex flex-col lg:flex-row justify-between items-center gap-5">

          <p className="text-gray-400 text-center lg:text-left">
            © 2026 Bharat Sahayak AI. All Rights Reserved.
          </p>

          <div className="flex gap-5 text-2xl">

            <span title="India">🇮🇳</span>

            <span title="Artificial Intelligence">🤖</span>

            <span title="Government Schemes">🏛️</span>

            <span title="Education">🎓</span>

            <span title="Agriculture">🌾</span>

            <span title="Healthcare">🏥</span>

          </div>

        </div>

        <div className="mt-6 text-center text-sm text-gray-500">

          Built with ❤️ using Next.js • FastAPI • PostgreSQL • Groq AI

        </div>

      </div>

    </footer>
  );
}