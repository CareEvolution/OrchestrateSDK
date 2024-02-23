export interface IHttpHandler {
  post<TIn, TOut>(path: string, body: TIn, headers?: { [key: string]: string }): Promise<TOut>;
  get<TOut>(path: string, headers?: { [key: string]: string }): Promise<TOut>;
}

export class HttpHandler implements IHttpHandler {
  constructor(
    private baseUrl: string,
    private defaultHeaders: { [key: string]: string },
  ) {}

  private mergeHeaders(headers?: { [key: string]: string }): { [key: string]: string } {
    return {
      ...this.defaultHeaders,
      ...(headers ?? {}),
    };
  }

  async post(
    path: string,
    body: any, // eslint-disable-line @typescript-eslint/no-explicit-any
    headers?: { [key: string]: string },
  ): Promise<any> {
    // eslint-disable-line @typescript-eslint/no-explicit-any
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

  async get(path: string, headers?: { [key: string]: string }): Promise<any> {
    // eslint-disable-line @typescript-eslint/no-explicit-any
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
