"use client";

import { useState } from "react";

export default function EligibilityPage() {
  const [occupation, setOccupation] = useState("");
  const [language, setLanguage] = useState("en");

  const handleSubmit = () => {
    alert("Next step: Connect this form to FastAPI /eligibility/check API");
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-green-100 py-10">

      <div className="max-w-6xl mx-auto bg-white rounded-3xl shadow-xl p-10">

        <h1 className="text-4xl font-bold text-center text-blue-700">
          🇮🇳 Bharat Sahayak AI
        </h1>

        <p className="text-center text-gray-600 mt-3 mb-10">
          Check your eligibility for Government Schemes
        </p>

        {/* Language */}

        <div className="mb-6">

          <label className="font-semibold">
            Preferred Language
          </label>

          <select
            className="w-full border rounded-xl p-3 mt-2"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          >

            <option value="en">English</option>
            <option value="hi">हिन्दी</option>
            <option value="te">తెలుగు</option>
            <option value="ta">தமிழ்</option>
            <option value="kn">ಕನ್ನಡ</option>
            <option value="ml">മലയാളം</option>
            <option value="mr">मराठी</option>
            <option value="gu">ગુજરાતી</option>
            <option value="bn">বাংলা</option>
            <option value="pa">ਪੰਜਾਬੀ</option>
            <option value="or">ଓଡ଼ିଆ</option>
            <option value="as">অসমীয়া</option>
            <option value="ur">اردو</option>
            <option value="sa">संस्कृतम्</option>
            <option value="kok">Konkani</option>
            <option value="mai">Maithili</option>
            <option value="doi">Dogri</option>
            <option value="ks">Kashmiri</option>
            <option value="ne">Nepali</option>
            <option value="mni">Manipuri</option>
            <option value="bodo">Bodo</option>
            <option value="sat">Santali</option>
            <option value="sd">Sindhi</option>
            <option value="lus">Mizo</option>
            <option value="other">Other</option>

          </select>

        </div>

        {/* Personal Details */}

        <div className="grid md:grid-cols-2 gap-5">

          <div>

            <label className="font-semibold">
              Full Name
            </label>

            <input
              className="w-full border rounded-xl p-3 mt-2"
              placeholder="Enter your name"
            />

          </div>

          <div>

            <label className="font-semibold">
              Age (Years)
            </label>

            <input
              type="number"
              className="w-full border rounded-xl p-3 mt-2"
            />

          </div>

          <div>

            <label className="font-semibold">
              Gender
            </label>

            <select className="w-full border rounded-xl p-3 mt-2">

              <option>Male</option>
              <option>Female</option>
              <option>Other</option>

            </select>

          </div>

          <div>

            <label className="font-semibold">
              Annual Income (₹ per year)
            </label>

            <input
              type="number"
              className="w-full border rounded-xl p-3 mt-2"
            />

          </div>

          <div>

            <label className="font-semibold">
              State
            </label>

            <input
              className="w-full border rounded-xl p-3 mt-2"
            />

          </div>

          <div>

            <label className="font-semibold">
              District
            </label>

            <input
              className="w-full border rounded-xl p-3 mt-2"
            />

          </div>

          <div>

            <label className="font-semibold">
              Category
            </label>

            <select className="w-full border rounded-xl p-3 mt-2">

              <option>General</option>
              <option>OBC</option>
              <option>SC</option>
              <option>ST</option>
              <option>EWS</option>

            </select>

          </div>

          <div>

            <label className="font-semibold">
              Occupation
            </label>

            <select
              value={occupation}
              onChange={(e) => setOccupation(e.target.value)}
              className="w-full border rounded-xl p-3 mt-2"
            >

              <option value="">Select Occupation</option>

              <option>Student</option>
              <option>Farmer</option>
              <option>Worker</option>
              <option>Teacher</option>
              <option>Doctor</option>
              <option>Engineer</option>
              <option>Government Employee</option>
              <option>Private Employee</option>
              <option>Business</option>
              <option>Self Employed</option>
              <option>Police</option>
              <option>Army</option>
              <option>Senior Citizen</option>
              <option>Widow</option>
              <option>Unemployed</option>
              <option>Other</option>

            </select>

          </div>

        </div>

        {/* Student */}

        {occupation === "Student" && (

          <div className="mt-8 bg-blue-50 rounded-2xl p-6">

            <h2 className="text-xl font-bold mb-5">
              🎓 Student Details
            </h2>

            <div className="grid md:grid-cols-2 gap-5">

              <input
                placeholder="Education Level"
                className="border rounded-xl p-3"
              />

              <input
                placeholder="Course"
                className="border rounded-xl p-3"
              />

              <input
                placeholder="College Name"
                className="border rounded-xl p-3"
              />

              <input
                placeholder="Year of Study"
                className="border rounded-xl p-3"
              />

            </div>

          </div>

        )}

        {/* Farmer */}

        {occupation === "Farmer" && (

          <div className="mt-8 bg-green-50 rounded-2xl p-6">

            <h2 className="text-xl font-bold mb-5">
              🌾 Farmer Details
            </h2>

            <div className="grid md:grid-cols-2 gap-5">

              <input
                placeholder="Land Area (Acres)"
                className="border rounded-xl p-3"
              />

              <input
                placeholder="Crop Type"
                className="border rounded-xl p-3"
              />

              <input
                placeholder="Irrigation Type"
                className="border rounded-xl p-3"
              />

              <input
                placeholder="Farmer ID"
                className="border rounded-xl p-3"
              />

            </div>

          </div>

        )}

        {/* Worker */}

        {occupation === "Worker" && (

          <div className="mt-8 bg-yellow-50 rounded-2xl p-6">

            <h2 className="text-xl font-bold mb-5">
              👷 Worker Details
            </h2>

            <div className="grid md:grid-cols-2 gap-5">

              <input
                placeholder="Employer Name"
                className="border rounded-xl p-3"
              />

              <input
                placeholder="Labour Card Number"
                className="border rounded-xl p-3"
              />

            </div>

          </div>

        )}

        {/* Checkboxes */}

        <div className="mt-8 grid md:grid-cols-2 gap-3">

          <label><input type="checkbox"/> Person with Disability</label>

          <label><input type="checkbox"/> Minority</label>

          <label><input type="checkbox"/> Ex Serviceman</label>

          <label><input type="checkbox"/> Pensioner</label>

          <label><input type="checkbox"/> Widow</label>

          <label><input type="checkbox"/> Orphan</label>

        </div>

        <button
          onClick={handleSubmit}
          className="mt-10 w-full bg-blue-700 hover:bg-blue-800 text-white py-4 rounded-xl text-xl font-semibold"
        >
          Check Eligibility
        </button>

      </div>

    </main>
  );
}