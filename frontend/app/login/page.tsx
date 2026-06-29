"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { loginUser } from "../../services/auth";

export default function LoginPage() {
  const router = useRouter();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [showPassword, setShowPassword] = useState(false);

  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    if (!email || !password) {
      alert("Please enter email and password.");
      return;
    }

    setLoading(true);

    try {
      const response = await loginUser({
        email,
        password,
      });

      localStorage.setItem("user", JSON.stringify(response));

      alert("Login Successful!");

      router.push("/dashboard");
    } catch (error: any) {
      alert(error.message);
    }

    setLoading(false);
  };

  return (
    <main className="min-h-screen hero flex items-center justify-center px-6 py-10">

      <div className="bg-white rounded-3xl shadow-2xl p-10 w-full max-w-md fade-in">

        <div className="text-center">

          <div className="text-6xl">
            🇮🇳
          </div>

          <h1 className="text-4xl font-bold text-blue-700 mt-3">
            Bharat Sahayak AI
          </h1>

          <p className="text-gray-500 mt-2">
            Login to continue
          </p>

        </div>

        <div className="mt-8">

          <label className="font-semibold">
            📧 Email
          </label>

          <input
            type="email"
            placeholder="Enter Email"
            className="mt-2 mb-5"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <label className="font-semibold">
            🔒 Password
          </label>

          <input
            type={showPassword ? "text" : "password"}
            placeholder="Enter Password"
            className="mt-2"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <div className="flex justify-between mt-3">

            <label className="flex gap-2 items-center text-sm">

              <input
                type="checkbox"
                checked={showPassword}
                onChange={() =>
                  setShowPassword(!showPassword)
                }
              />

              Show Password

            </label>

            <Link
              href="/forgot-password"
              className="text-blue-700 text-sm"
            >
              Forgot Password?
            </Link>

          </div>

          <button
            onClick={handleLogin}
            disabled={loading}
            className="btn-primary mt-8 w-full"
          >
            {loading ? "Logging In..." : "Login"}
          </button>

          <div className="text-center mt-8">

            <p>
              Don't have an account?
            </p>

            <Link href="/register">

              <button className="btn-success mt-4 w-full">
                Create New Account
              </button>

            </Link>

          </div>

        </div>

      </div>

    </main>
  );
}