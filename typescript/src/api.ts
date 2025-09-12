import { ConvertApi } from "./convert.js";
import { IHttpHandler } from "./httpHandler.js";
import { createHttpHandler } from "./httpHandlerFactory.js";
import { InsightApi } from "./insight.js";
import { TerminologyApi } from "./terminology.js";

export interface Configuration {
  apiKey?: string;
  timeoutMs?: number;
}

export class OrchestrateApi {
  readonly terminology: TerminologyApi;
  readonly convert: ConvertApi;
  readonly insight: InsightApi;

  /**
   * Exposes the underlying IHttpHandler instance for advanced usage. This is
   * made available to take advantage of features not yet wrapped in
   * OrchestrateApi. This may change without warning.
   * @deprecated Not a stable API.
   */
  readonly httpHandler: IHttpHandler;

  constructor(configuration: Configuration | undefined = {}) {
    const httpHandler = createHttpHandler(configuration.apiKey, undefined, configuration.timeoutMs);

    this.terminology = new TerminologyApi(httpHandler);
    this.convert = new ConvertApi(httpHandler);
    this.insight = new InsightApi(httpHandler);

    this.httpHandler = httpHandler;
  }
}
