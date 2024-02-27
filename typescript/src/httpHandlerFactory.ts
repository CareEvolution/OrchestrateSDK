import { HttpHandler, IHttpHandler } from "./httpHandler";

function getPriorityBaseUrl(): string {
  return process.env.ORCHESTRATE_BASE_URL || "https://api.careevolutionapi.com";
}

function getPriorityApiKey(apiKey: string | undefined): string | undefined {
  return apiKey || process.env.ORCHESTRATE_API_KEY;
}

function getAdditionalHeaders(): { [key: string]: string; } | undefined {
  if (process.env.ORCHESTRATE_ADDITIONAL_HEADERS) {
    return JSON.parse(process.env.ORCHESTRATE_ADDITIONAL_HEADERS);
  }
  return undefined;
}

export function createHttpHandler(
  apiKey: string | undefined,
): IHttpHandler {
  const baseUrl = getPriorityBaseUrl();
  const additionalHeaders = getAdditionalHeaders();

  const defaultHeaders = {
    ...(additionalHeaders ?? {}),
    ...{
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  } as { [key: string]: string; };

  const priorityApiKey = getPriorityApiKey(apiKey);
  if (priorityApiKey) {
    defaultHeaders["x-api-key"] = priorityApiKey;
  }

  return new HttpHandler(baseUrl, defaultHeaders);
}
