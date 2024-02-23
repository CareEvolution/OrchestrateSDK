import { ConvertApi } from "./convert";
import { createHttpHandler } from "./httpHandlerFactory";
import { InsightApi } from "./insight";
import { TerminologyApi } from "./terminology";

export interface Configuration {
  apiKey?: string;
  baseUrl?: string;
  additionalHeaders?: { [key: string]: string; };
}

export class OrchestrateApi {
  terminology: TerminologyApi;
  convert: ConvertApi;
  insight: InsightApi;

  constructor(configuration: Configuration) {
    const httpHandler = createHttpHandler(
      configuration.baseUrl,
      configuration.apiKey,
      configuration.additionalHeaders
    );

    this.terminology = new TerminologyApi(httpHandler);
    this.convert = new ConvertApi(httpHandler);
    this.insight = new InsightApi(httpHandler);
  }
}
