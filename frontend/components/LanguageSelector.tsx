"use client";

type LanguageSelectorProps = {
  value: string;
  onChange: (value: string) => void;
};

const languages = [
  { code: "en", name: "English 🇬🇧" },
  { code: "hi", name: "हिन्दी 🇮🇳" },
  { code: "te", name: "తెలుగు 🇮🇳" },
  { code: "ta", name: "தமிழ் 🇮🇳" },
  { code: "kn", name: "ಕನ್ನಡ 🇮🇳" },
  { code: "ml", name: "മലയാളം 🇮🇳" },
  { code: "mr", name: "मराठी 🇮🇳" },
  { code: "gu", name: "ગુજરાતી 🇮🇳" },
  { code: "bn", name: "বাংলা 🇮🇳" },
  { code: "pa", name: "ਪੰਜਾਬੀ 🇮🇳" },
  { code: "or", name: "ଓଡ଼ିଆ 🇮🇳" },
  { code: "as", name: "অসমীয়া 🇮🇳" },
  { code: "ur", name: "اردو 🇮🇳" },
  { code: "sa", name: "संस्कृतम् 🇮🇳" },
  { code: "kok", name: "Konkani 🇮🇳" },
  { code: "mai", name: "Maithili 🇮🇳" },
  { code: "doi", name: "Dogri 🇮🇳" },
  { code: "ks", name: "Kashmiri 🇮🇳" },
  { code: "ne", name: "Nepali 🇮🇳" },
  { code: "mni", name: "Manipuri 🇮🇳" },
  { code: "bodo", name: "Bodo 🇮🇳" },
  { code: "sat", name: "Santali 🇮🇳" },
  { code: "sd", name: "Sindhi 🇮🇳" },
  { code: "lus", name: "Mizo 🇮🇳" },
  { code: "other", name: "Other Language 🌍" },
];

export default function LanguageSelector({
  value,
  onChange,
}: LanguageSelectorProps) {
  return (
    <div>

      <label className="block text-lg font-semibold text-gray-700 mb-2">
        🌐 Preferred Language
      </label>

      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="
          w-full
          rounded-xl
          border-2
          border-blue-300
          bg-white
          px-4
          py-3
          text-lg
          shadow-md
          focus:border-blue-600
          focus:outline-none
          focus:ring-4
          focus:ring-blue-200
          transition
        "
      >
        {languages.map((language) => (
          <option
            key={language.code}
            value={language.code}
          >
            {language.name}
          </option>
        ))}
      </select>

      <p className="text-sm text-gray-500 mt-2">
        💡 Choose your preferred language. AI responses and eligibility results
        will be shown in this language whenever available.
      </p>

    </div>
  );
}