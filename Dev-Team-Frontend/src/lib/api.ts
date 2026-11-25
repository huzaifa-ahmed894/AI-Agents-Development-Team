import { parseRun } from "./contracts";

// Browser -> Next.js proxy (/api/team/...) -> FastAPI. No API key in the browser.
async function request(path: string, init?: RequestInit) {
  let response: Response;
  try {
    response = await fetch(`/api/team/${path}`, { ...init, cache: "no-store" });
  } catch {
    throw new Error("Couldn’t reach the app server. Check your connection.");
  }
  const body: unknown = await response.json().catch(() => null);
  if (!response.ok) {
    const error = body && typeof body === "object" && "error" in body && typeof body.error === "string" ? body.error : null;
    throw new Error(error || "Something went wrong. Please try again.");
  }
  return parseRun(body);
}

export const createRun = (message: string, parentId: string | null) => request("chat", {
  method: "POST", headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message, parent_id: parentId }),
});

export const getRun = (id: string) => request(`runs/${encodeURIComponent(id)}`);

export const downloadUrl = (id: string) => `/api/team/runs/${encodeURIComponent(id)}/download`;
