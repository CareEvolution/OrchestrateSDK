import { OrchestrateClientError, OrchestrateHttpError } from "./exceptions.js";

export interface IHttpHandler {
  post<TIn, TOut>(path: string, body: TIn, headers?: { [key: string]: string; }): Promise<TOut>;
  get<TOut>(path: string, headers?: { [key: string]: string; }): Promise<TOut>;
}

class OperationalOutcomeIssue {
  severity: string | undefined;
  code: string | undefined;
  diagnostics: string | undefined;
}

async function readJsonOutcomes(responseText: string): Promise<OperationalOutcomeIssue[]> {
  try {
    const json = JSON.parse(responseText);
    if (json.issue) {
      return json.issue;
    }
    if (json.type === "https://tools.ietf.org/html/rfc9110#section-15.5.1") {
      return [{
        severity: "error",
        code: json.title,
        diagnostics: json.detail,
      }];
    }
    return [];
  }
  catch (e) {
    return [];
  }
}

async function readOperationalOutcomes(responseText: string): Promise<string[]> {
  const outcomes = await readJsonOutcomes(responseText);
  if (outcomes.length > 0) {
    return outcomes.map((o) => `${o.severity}: ${o.code} - ${o.diagnostics}`);
  }
  return [responseText];
}

async function errorFromResponse(response: Response): Promise<never> {
  const responseText = await response.text();
  const operationalOutcomes = await readOperationalOutcomes(responseText);
  if (response.status >= 400 && response.status < 600) {
    throw new OrchestrateClientError(responseText, operationalOutcomes);
  }

  throw new OrchestrateHttpError(responseText);
}

export class HttpHandler implements IHttpHandler {
  constructor(
    private baseUrl: string,
    private defaultHeaders: { [key: string]: string; },
    private timeoutMs: number,
  ) { }

  private mergeHeaders(headers?: { [key: string]: string; }): { [key: string]: string; } {
    return {
      ...this.defaultHeaders,
      ...(headers ?? {}),
    };
  }

  toString(): string {
    return this.baseUrl;
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
      signal: this.timeoutMs ? AbortSignal.timeout(this.timeoutMs) : undefined,
    });
    if (!response.ok) {
      await errorFromResponse(response);
    }

    if (requestHeaders["Accept"] === "application/zip" || requestHeaders["Accept"] === "application/pdf") {
      return await response.arrayBuffer();
    }

    if (requestHeaders["Accept"] === "application/json") {
      return await response.json();
    }
    return await response.text();
  }

  async get(path: string, headers?: { [key: string]: string; }): Promise<any> { // eslint-disable-line @typescript-eslint/no-explicit-any
    const requestHeaders = this.mergeHeaders(headers);

    const url = this.baseUrl + path;
    const response = await fetch(url, {
      method: "GET",
      headers: requestHeaders,
      signal: this.timeoutMs ? AbortSignal.timeout(this.timeoutMs) : undefined,
    });
    if (!response.ok) {
      await errorFromResponse(response);
    }

    return await response.json();
  }
}
