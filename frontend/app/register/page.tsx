"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { registerUser } from "../../services/auth";

export default function RegisterPage() {
  const router = useRouter();

  const [form, setForm] = useState({
    first_name: "",
    last_name: "",
    email: "",
    phone_number: "",
    password: "",
    confirm_password: "",
  });

  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);

  function handleChange(
    e: React.ChangeEvent<HTMLInputElement>
  ) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  async function handleRegister() {
    if (
      !form.first_name ||
      !form.last_name ||
      !form.email ||
      !form.phone_number ||
      !form.password
    ) {
      alert("Please fill all required fields.");
      return;
    }

    if (form.password !== form.confirm_password) {
      alert("Passwords do not match.");
      return;
    }

    setLoading(true);

    try {
      await registerUser({
        first_name: form.first_name,
        last_name: form.last_name,
        email: form.email,
        phone_number: form.phone_number,
        password: form.password,
      });

      alert("Registration Successful!");

      router.push("/login");
    } catch (error: any) {
      alert(error.message);
    }

    setLoading(false);
  }

  return (
    <main className="min-h-screen hero flex items-center justify-center px-6 py-10">

      <div className="bg-white rounded-3xl shadow-2xl p-10 w-full max-w-lg fade-in">

        <div className="text-center">

          <div className="text-6xl">
            🇮🇳
          </div>

          <h1 className="text-4xl font-bold text-blue-700 mt-3">
            Bharat Sahayak AI
          </h1>

          <p className="text-gray-500 mt-2">
            Create Your Account
          </p>

        </div>

        <div className="mt-8 space-y-5">

          <div className="grid md:grid-cols-2 gap-4">

            <input
              name="first_name"
              placeholder="👤 First Name"
              value={form.first_name}
              onChange={handleChange}
            />

            <input
              name="last_name"
              placeholder="👤 Last Name"
              value={form.last_name}
              onChange={handleChange}
            />

          </div>

          <input
            name="email"
            type="email"
            placeholder="📧 Email Address"
            value={form.email}
            onChange={handleChange}
          />

          <input
            name="phone_number"
            placeholder="📱 Phone Number"
            value={form.phone_number}
            onChange={handleChange}
          />

          <input
            name="password"
            type={showPassword ? "text" : "password"}
            placeholder="🔒 Password"
            value={form.password}
            onChange={handleChange}
          />

          <input
            name="confirm_password"
            type={showPassword ? "text" : "password"}
            placeholder="🔒 Confirm Password"
            value={form.confirm_password}
            onChange={handleChange}
          />

          <label className="flex items-center gap-2">

            <input
              type="checkbox"
              checked={showPassword}
              onChange={() =>
                setShowPassword(!showPassword)
              }
            />

            Show Password

          </label>

          <button
            onClick={handleRegister}
            disabled={loading}
            className="btn-primary w-full"
          >
            {loading
              ? "Creating Account..."
              : "Create Account"}
          </button>

          <div className="text-center">

            <p className="text-gray-600">
              Already have an account?
            </p>

            <Link href="/login">

              <button className="btn-success mt-4 w-full">
                Login
              </button>

            </Link>

          </div>

        </div>

      </div>

    </main>
  );
}