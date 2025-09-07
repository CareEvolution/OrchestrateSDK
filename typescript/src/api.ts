import { ConvertApi } from "./convert.js";
import { createHttpHandler } from "./httpHandlerFactory.js";
import { InsightApi } from "./insight.js";
import { TerminologyApi } from "./terminology.js";

export interface Configuration {
  apiKey?: string;
  timeoutMs?: number;
}

export class OrchestrateApi {
  terminology: TerminologyApi;
  convert: ConvertApi;
  insight: InsightApi;

  constructor(configuration: Configuration | undefined = {}) {
    const httpHandler = createHttpHandler(configuration.apiKey, undefined, configuration.timeoutMs);

    this.terminology = new TerminologyApi(httpHandler);
    this.convert = new ConvertApi(httpHandler);
    this.insight = new InsightApi(httpHandler);
  }
}
