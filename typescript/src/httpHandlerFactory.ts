import { HttpHandler, IHttpHandler } from "./httpHandler";

function getPriorityBaseUrl(baseUrl: string | undefined): string {
    if (baseUrl) {
      return baseUrl;
    }
    if (process.env.ORCHESTRATE_BASE_URL) {
      return process.env.ORCHESTRATE_BASE_URL;
    }
    return "https://api.careevolutionapi.com";
  }
  
  function getPriorityApiKey(apiKey: string | undefined): string | undefined {
    if (apiKey) {
      return apiKey;
    }
    if (process.env.ORCHESTRATE_API_KEY) {
      return process.env.ORCHESTRATE_API_KEY;
    }
    return undefined;
  }
  

export function createHttpHandler(
    baseUrl: string | undefined,
    apiKey: string | undefined,
    additionalHeaders: { [key: string]: string; } | undefined,
  ): IHttpHandler {
    const defaultHeaders = {
      ...additionalHeaders ?? {},
      ...{
        "Content-Type": "application/json",
        "Accept": "application/json",
      }
    } as { [key: string]: string; };
  
    const priorityApiKey = getPriorityApiKey(apiKey);
    if (priorityApiKey) {
      defaultHeaders["x-api-key"] = priorityApiKey;
    }
  
    const priorityBaseUrl = getPriorityBaseUrl(baseUrl);
  
    return new HttpHandler(priorityBaseUrl, defaultHeaders);
  }
  