import { Advisories } from "./advisories.js";
import { IHttpHandler } from "../httpHandler.js";
import { createLocalHashingHttpHandler } from "../httpHandlerFactory.js";
import { BlindedDemographic, Demographic } from "./demographic.js";

export type HashDemographicResponse = BlindedDemographic & {
  advisories: Advisories;
};

export type LocalHashingApiConfiguration = {
  url?: string | undefined;
};

export class LocalHashingApi {
  private httpHandler: IHttpHandler;

  constructor(configuration: LocalHashingApiConfiguration = {}) {
    this.httpHandler = createLocalHashingHttpHandler(configuration.url);
  }

  toString(): string {
    return `LocalHashingApi(${this.httpHandler.toString()})`;
  }

  /**
   * Hashes a demographic using the local hashing service.
   * @param demographic The demographic to hash.
   * @returns The hashed demographic.

        - `data`: The B64 encoded hash provided by the local hashing service.
        - `version`: The version number provided by the local hashing service.
        - `advisories`: Contains advisory messages about the operation.

   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/condition.html
   */
  public async hash(demographic: Demographic): Promise<HashDemographicResponse> {
    return this.httpHandler.post("/hash", demographic);
  }
}
