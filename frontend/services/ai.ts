import { apiRequest } from "./api";

export async function chatWithAI(message: string) {
  return await apiRequest(
    "/ai/chat",
    "POST",
    {
      message,
    }
  );
}

export async function summarizeText(text: string) {
  return await apiRequest(
    "/ai/summarize",
    "POST",
    {
      text,
    }
  );
}

export async function classifyIntent(text: string) {
  return await apiRequest(
    "/ai/classify",
    "POST",
    {
      text,
    }
  );
}

export async function extractEntities(text: string) {
  return await apiRequest(
    "/ai/entities",
    "POST",
    {
      text,
    }
  );
}