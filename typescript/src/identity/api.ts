import { IHttpHandler } from "../httpHandler.js";
import { createIdentityHttpHandler } from "../httpHandlerFactory.js";
import { Advisories } from "./advisories.js";
import { BlindedDemographic, Demographic } from "./demographic.js";
import { IdentityMonitoringApi } from "./monitoring.js";

export type PersonStatus = {
  code: string;
  supercededBy: string[];
};

export type Record = {
  source: string;
  identifier: string;
};

export type Person = {
  id: string;
  records: Record[];
  version: number;
  status: PersonStatus;
};

export type AddOrUpdateRecordRequest = Record & {
  demographic: Demographic;
};

export type AddOrUpdateBlindedRecordRequest = Record & {
  blindedDemographic: BlindedDemographic;
};

export type MatchedPersonReference = {
  matchedPerson: Person;
  changedPersons: Person[];
};

export type AddOrUpdateRecordResponse = MatchedPersonReference & {
  advisories: Advisories;
};

export type AddOrUpdateBlindedRecordResponse = MatchedPersonReference;

export type GetPersonByRecordResponse = Person;

export type GetPersonByIDRequest = {
  id: string;
};

export type GetPersonByIDResponse = Person;


export type MatchDemographicsResponse = {
  matchedPersons: Person[];
  advisories: Advisories[];
};

export type MatchDemographicsRequest = Demographic;


export type MatchBlindedDemographicRequest = BlindedDemographic;


export type MatchBlindedDemographicsResponse = {
  matchedPersons: Person[];
};

export type DeleteRecordRequest = Record;

export type DeleteRecordResponse = {
  changedPersons: Person[];
};

export type MatchGuidanceRequest = {
  recordOne: Record;
  recordTwo: Record;
  comment: string;
};

export type AddMatchGuidanceRequest = MatchGuidanceRequest & {
  action: "Match" | "NoMatch";
};

export type AddMatchGuidanceResponse = {
  changedPersons: Person[];
};

export type RemoveMatchGuidanceRequest = MatchGuidanceRequest;

export type RemoveMatchGuidanceResponse = {
  changedPersons: Person[];
};

export type GetPersonByRecordRequest = Record;

export type IdentityApiConfiguration = {
  url?: string | undefined;
  apiKey?: string | undefined;
  metricsKey?: string | undefined;
};

function buildSourceIdentifierRoute(source: string, identifier: string): string {
  return `${encodeURIComponent(source)}/${encodeURIComponent(identifier)}`;
}

export class IdentityApi {
  private httpHandler: IHttpHandler;
  public monitoring: IdentityMonitoringApi;

  constructor(configuration: IdentityApiConfiguration = {}) {
    this.httpHandler = createIdentityHttpHandler(configuration.apiKey, configuration.metricsKey, configuration.url);
    this.monitoring = new IdentityMonitoringApi(this.httpHandler);
  }

  toString(): string {
    return `IdentityApi(${this.httpHandler.toString()})`;
  }

  /**
   * Adds a new record or updates a previously created one.
   * @param request The request to add or update a record.
   *  - `source` The system from which the record demographics were sourced.
   *  - `identifier` The unique identifier of the record within the source.
   *  - `demographic` The demographic information of the record.
   * @returns The record's assigned person ID, along with any changes resulting from the addition or update.
   * @link https://orchestrate.docs.careevolution.com/identity/operations/add_update_record.html
   */
  public async addOrUpdateRecord(request: AddOrUpdateRecordRequest): Promise<AddOrUpdateRecordResponse> {
    const sourceIdentifierRoute = buildSourceIdentifierRoute(request.source, request.identifier);
    return this.httpHandler.post(`/mpi/v1/record/${sourceIdentifierRoute}`, request.demographic);
  }

  /**
   * Adds a new record or updates a previously created one in privacy-preserving (blinded) mode.
   * @param request The request to add or update a record.
   *  - `source`: The system from which the record demographics were sourced.
      - `identifier`: The unique identifier of the record within the source.
      - `data`: The B64 encoded hash provided by the local hashing service.
      - `version`: The version number provided by the local hashing service.
   * @returns Returns the record's assigned person ID, along with any changes resulting from the addition or update.
   * @link https://orchestrate.docs.careevolution.com/identity/operations/add_update_record_blinded.html
   */
  public async addOrUpdateBlindedRecord(request: AddOrUpdateBlindedRecordRequest): Promise<AddOrUpdateBlindedRecordResponse> {
    const sourceIdentifierRoute = buildSourceIdentifierRoute(request.source, request.identifier);
    console.log(sourceIdentifierRoute);
    const payload = {
      data: request.blindedDemographic.data,
      version: request.blindedDemographic.version
    };
    return this.httpHandler.post(`/mpi/v1/blindedRecord/${sourceIdentifierRoute}`, payload);
  }

  /**
   * Given a source system and identifier, this retrieves the person's metadata (including their Person ID) and the collection of records grouped with that individual.
   * @param request The request to get a person by record.
   *  - `source`: The system from which the record demographics were sourced.
      - `identifier`: The unique identifier of the record within the source.
   * @returns The matched person.
   * @link https://orchestrate.docs.careevolution.com/identity/operations/get_person_by_record.html
   */
  public async getPersonByRecord(request: GetPersonByRecordRequest): Promise<GetPersonByRecordResponse> {
    const sourceIdentifierRoute = buildSourceIdentifierRoute(request.source, request.identifier);
    return this.httpHandler.get(`/mpi/v1/record/${sourceIdentifierRoute}`);
  }

  /**
   * Given a Person ID, this retrieves the person's metadata and the collection of records grouped with that individual.
   * @param reuest The request to get a person by ID.
   * - `id`: id of the person to fetch
   * @returns The matched person.
   * @link https://orchestrate.docs.careevolution.com/identity/operations/get_person_by_id.html
   */
  public async getPersonByID(request: GetPersonByIDRequest): Promise<GetPersonByIDResponse> {
    return this.httpHandler.get(`/mpi/v1/person/${encodeURIComponent(request.id)}`);
  }

  /**
   * Finds all persons and their associated records that match the provided demographics. This operation is read-only, and will not create or update any person records.
   * @param request The demographic The demographic to match.
   * @returns Persons and their associated records that match the provided demographics.
   * @link https://orchestrate.docs.careevolution.com/identity/operations/match_demographics.html
   */
  public async matchDemographics(demographic: MatchDemographicsRequest): Promise<MatchDemographicsResponse> {
    return this.httpHandler.post("/mpi/v1/match", demographic);
  }

  /**
   * Finds all persons and their associated records that match the provided demographics in privacy-preserving (blinded) mode.
   * @param request The blinded demographic to match
   * @returns Persons and their associated records that match the provided demographics.
   * @link https://orchestrate.docs.careevolution.com/identity/operations/match_demographics_blinded.html
   */
  public async matchBlindedDemographics(demographic: MatchBlindedDemographicRequest): Promise<MatchBlindedDemographicsResponse> {
    return this.httpHandler.post("/mpi/v1/matchBlinded", demographic);
  }

  /**
   * Deletes a record using a source system and identifier.
   * @param request The request to delete a record.
   * - `source`: The system from which the record demographics were sourced.
   * - `identifier`: The unique identifier of the record within the source.
   * @returns List of persons changed by the operation.
   * @link https://orchestrate.docs.careevolution.com/identity/operations/delete_record.html
   */
  public async deleteRecord(request: DeleteRecordRequest): Promise<DeleteRecordResponse> {
    const sourceIdentifierRoute = buildSourceIdentifierRoute(request.source, request.identifier);
    return this.httpHandler.post(`/mpi/v1/deleteRecord/${sourceIdentifierRoute}`, {});
  }

  /**
   * Overrides automatic matching with manual guidance for a particular set of records.
   * @param personId The persons to add match guidance for.
   * - `record_one`: The first record
   * - `record_two`: The second record
   * - `action`: Use Match if the two records represent the same individual, and NoMatch if the two records represent different individuals.
   * - `comment`: A comment for documentation/audit purposes.
   * @returns List of persons changed by the operation.
   * @link https://orchestrate.docs.careevolution.com/identity/operations/add_guidance.html
   */
  public async addMatchGuidance(request: AddMatchGuidanceRequest): Promise<AddMatchGuidanceResponse> {
    return this.httpHandler.post(`/mpi/v1/addGuidance`, request);
  }

  /**
   * Removes a previously-created manual match guidance.
   * @param personId The persons to remove match guidance for.
   * - `record_one`: The first record
   * - `record_two`: The second record
   * - `comment`: A comment for documentation/audit purposes.
   * @returns List of persons changed by the operation.
   * @link https://orchestrate.docs.careevolution.com/identity/operations/remove_guidance.html
   */
  public async removeMatchGuidance(request: RemoveMatchGuidanceRequest): Promise<RemoveMatchGuidanceResponse> {
    return this.httpHandler.post(`/mpi/v1/removeGuidance`, request);
  }


}