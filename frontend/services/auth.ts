import { apiRequest } from "./api";

export async function registerUser(user: {
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
  password: string;
}) {
  return await apiRequest(
    "/auth/register",
    "POST",
    user
  );
}

export async function loginUser(credentials: {
  email: string;
  password: string;
}) {
  return await apiRequest(
    "/auth/login",
    "POST",
    credentials
  );
}

export async function logoutUser() {
  localStorage.removeItem("user");
}