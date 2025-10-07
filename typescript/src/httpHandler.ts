import { OrchestrateClientError, OrchestrateHttpError } from "./exceptions.js";

export interface IHttpHandler {
  post<TIn, TOut>(path: string, body: TIn, headers?: { [key: string]: string; }): Promise<TOut>;
  get<TOut>(path: string, headers?: { [key: string]: string; }): Promise<TOut>;
}

class OperationalOutcomeIssue {
  severity: string;
  code: string;
  diagnostics: string;
  details: string;

  constructor(severity: string, code: string, diagnostics: string, details: string) {
    this.severity = severity;
    this.code = code;
    this.diagnostics = diagnostics;
    this.details = details;
  }

  toString(): string {
    let s = `${this.severity}: ${this.code}`;
    const message = [this.details, this.diagnostics]
      .filter(msg => msg)
      .join("; ");
    if (message) {
      s += ` - ${message}`;
    }
    return s;
  }
}

function getIssueDetailString(detail: any): string { // eslint-disable-line @typescript-eslint/no-explicit-any
  if (detail?.text) {
    return detail.text;
  }
  if (detail?.coding && Array.isArray(detail.coding)) {
    for (const coding of detail.coding) {
      const codingString = getDetailCodingString(coding);
      if (codingString) {
        return codingString;
      }
    }
  }
  return "";
}

function getDetailCodingString(coding: any): string { // eslint-disable-line @typescript-eslint/no-explicit-any
  const parts = [coding?.code, coding?.display].filter(s => s);
  return parts.join(": ");
}

async function readJsonOutcomes(responseText: string): Promise<OperationalOutcomeIssue[]> {
  try {
    const json = JSON.parse(responseText);
    if (json.issue) {
      return json.issue.map((issue: any) => // eslint-disable-line @typescript-eslint/no-explicit-any
        new OperationalOutcomeIssue(
          issue.severity || "",
          issue.code || "",
          issue.diagnostics || "",
          getIssueDetailString(issue.details || {})
        )
      );
    }
    if (json.type === "https://tools.ietf.org/html/rfc9110#section-15.5.1") {
      return [new OperationalOutcomeIssue(
        "error",
        json.title || "",
        json.detail || "",
        ""
      )];
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
    return outcomes.map((o) => o.toString());
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
