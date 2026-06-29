const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "https://bharat-sahayak-ai-backend.onrender.com";

export async function apiRequest(
  endpoint: string,
  method: string = "GET",
  body?: any
) {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method,
    headers: {
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Something went wrong");
  }

  return data;
}

export default API_BASE_URL;