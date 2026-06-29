"use client";

import Link from "next/link";

const schemes = [
  {
    id: 1,
    name: "Pragati Scholarship",
    category: "Education",
    ministry: "AICTE",
    score: 96,
    benefits: "Financial assistance up to ₹50,000 per year.",
    documents: [
      "Aadhaar Card",
      "Income Certificate",
      "Bonafide Certificate",
      "Bank Passbook",
      "Passport Size Photograph",
    ],
    apply: "https://www.aicte-india.org/",
  },
  {
    id: 2,
    name: "PM Kisan",
    category: "Agriculture",
    ministry: "Ministry of Agriculture",
    score: 90,
    benefits: "₹6000 per year financial assistance.",
    documents: [
      "Aadhaar Card",
      "Land Records",
      "Bank Passbook",
    ],
    apply: "https://pmkisan.gov.in/",
  },
];

export default function ResultsPage() {
  return (
    <main className="min-h-screen bg-gray-100 py-10">

      <div className="max-w-7xl mx-auto">

        <h1 className="text-4xl font-bold text-center text-blue-700">
          Eligible Government Schemes
        </h1>

        <p className="text-center text-gray-600 mt-3 mb-10">
          Based on your profile, these schemes match your eligibility.
        </p>

        <div className="grid lg:grid-cols-2 gap-8">

          {schemes.map((scheme) => (

            <div
              key={scheme.id}
              className="bg-white rounded-3xl shadow-xl p-8"
            >

              <div className="flex justify-between">

                <div>

                  <h2 className="text-2xl font-bold">
                    {scheme.name}
                  </h2>

                  <p className="text-blue-600 mt-1">
                    {scheme.category}
                  </p>

                </div>

                <div className="text-right">

                  <p className="text-sm text-gray-500">
                    Match Score
                  </p>

                  <h2 className="text-4xl font-bold text-green-600">
                    {scheme.score}%
                  </h2>

                </div>

              </div>

              <hr className="my-6" />

              <h3 className="font-semibold">
                Ministry
              </h3>

              <p className="mb-5">
                {scheme.ministry}
              </p>

              <h3 className="font-semibold">
                Benefits
              </h3>

              <p className="mb-5">
                {scheme.benefits}
              </p>

              <h3 className="font-semibold">
                Required Documents
              </h3>

              <ul className="list-disc ml-6 mt-3 mb-6">

                {scheme.documents.map((doc, index) => (

                  <li key={index}>
                    {doc}
                  </li>

                ))}

              </ul>

              <div className="bg-blue-50 rounded-xl p-5">

                <h3 className="font-bold mb-2">
                  🤖 AI Explanation
                </h3>

                <p>
                  According to your profile, you satisfy most eligibility
                  conditions for this scheme. Please verify the required
                  documents before submitting your application.
                </p>

              </div>

              <div className="grid grid-cols-2 gap-4 mt-8">

                <a
                  href={scheme.apply}
                  target="_blank"
                  className="bg-blue-700 text-white text-center py-3 rounded-xl font-semibold"
                >
                  Apply Now
                </a>

                <button
                  className="border border-blue-700 text-blue-700 rounded-xl font-semibold"
                >
                  ❤️ Save
                </button>

              </div>

            </div>

          ))}

        </div>

        <div className="text-center mt-10">

          <Link href="/dashboard">

            <button
              className="bg-gray-800 text-white px-8 py-3 rounded-xl"
            >
              Back to Dashboard
            </button>

          </Link>

        </div>

      </div>

    </main>
  );
}