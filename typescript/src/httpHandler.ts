export interface IHttpHandler {
  post<TIn, TOut>(path: string, body: TIn, headers?: { [key: string]: string; }): Promise<TOut>;
  get<TOut>(path: string, headers?: { [key: string]: string; }): Promise<TOut>;
}

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

export class HttpHandler implements IHttpHandler {
  baseUrl: string;
  defaultHeaders: { [key: string]: string; };

  constructor(baseUrl: string, headers: { [key: string]: string; }) {
    this.baseUrl = baseUrl;
    this.defaultHeaders = headers;
  }

  private mergeHeaders(headers?: { [key: string]: string; }): { [key: string]: string; } {
    return {
      ...this.defaultHeaders,
      ...headers ?? {},
    };
  }

  async post(
    path: string,
    body: any, // eslint-disable-line @typescript-eslint/no-explicit-any
    headers?: { [key: string]: string; },
  ): Promise<any> { // eslint-disable-line @typescript-eslint/no-explicit-any
    const requestHeaders = this.mergeHeaders(headers);

    const preparedBody = requestHeaders["Content-Type"] === "application/json" ? JSON.stringify(body) : body;
    const url = this.baseUrl + path;

    const response = await fetch(url, {
      method: "POST",
      headers: requestHeaders,
      body: preparedBody,
    });
    if (!response.ok) {
      throw new Error(await response.text());
    }

    if (requestHeaders["Accept"] === "application/zip" || requestHeaders["Accept"] === "application/pdf") {
      return await response.arrayBuffer();
    }

    if (requestHeaders["Accept"] === "application/json") {
      return await response.json();
    }
    return await response.text();
  }

  async get(
    path: string,
    headers?: { [key: string]: string; },
  ): Promise<any> { // eslint-disable-line @typescript-eslint/no-explicit-any
    const requestHeaders = this.mergeHeaders(headers);

    const url = this.baseUrl + path;
    const response = await fetch(url, {
      method: "GET",
      headers: requestHeaders,
    });
    if (!response.ok) {
      throw new Error(await response.text());
    }

    return await response.json();
  }
}
