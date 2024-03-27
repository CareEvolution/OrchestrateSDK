import { IHttpHandler } from "../httpHandler.js";

type IdentifierMetricsRecordType =
  "City" |
  "DOB" |
  "Email" |
  "FirstName" |
  "Gender" |
  "HighwayNumber" |
  "HighwayPrefix" |
  "LastFourSSN" |
  "LastName" |
  "MaidenName" |
  "MiddleName" |
  "Ordinal" |
  "PO" |
  "POBoxNumber" |
  "PhoneNumber" |
  "SSN" |
  "State" |
  "StreetFraction" |
  "StreetName" |
  "StreetNumber" |
  "StreetNumberAlpha" |
  "StreetType" |
  "UnitNumber" |
  "UnitNumberAlpha" |
  "UnitType" |
  "ZipCode" |
  "ZipCodeExtension";

export type IdentifierMetricsRecord = {
  identifierType: IdentifierMetricsRecordType;
  recordCount: number;
  recordRatio: number;
  source: string;
};

export type GlobalIdentifierMetricsRecord = IdentifierMetricsRecord & {
  source: "";
};

export type SourceTotal = {
  source: string;
  totalRecordCount: number;
};

export type IdentifierMetricsResponse = {
  refreshed: string;
  totalRecordCount: number;
  totalPersonCount: number;
  globalMetricsRecords: GlobalIdentifierMetricsRecord[];
  summaryMetricsRecords: IdentifierMetricsRecord[];
  sourceTotals: SourceTotal[];
};

export type DatasourceOverlapRecord = {
  datasourceA: string;
  datasourceB: string;
  overlapCount: number;
};

export type OverlapMetricsResponse = {
  datasourceOverlapRecords: DatasourceOverlapRecord[];
};


export class IdentityMonitoringApi {
  constructor(private readonly httpHandler: IHttpHandler) { }

  toString(): string {
    return `IdentityMonitoringApi(${this.httpHandler.toString()})`;
  }

  /**
   * Queries identifier metrics. The identifier metrics help you understand:
   * - How many records you have stored.
   * - How often different kinds of demographic identifiers are found in your records.
   * - What kind and how many demographic identifiers different data sources provide.
   * @returns The identifier metrics.
   * @link https://orchestrate.docs.careevolution.com/identity/metrics/identifier.html
   */
  public async identifierMetrics(): Promise<IdentifierMetricsResponse> {
    return this.httpHandler.get("/monitoring/v1/identifierMetrics");
  }

  /**
   * Queries overlap metrics. The overlap metrics help you understand how many patients have records in multiple source systems.
   * @returns The overlap metrics.
   * @link https://orchestrate.docs.careevolution.com/identity/metrics/overlap.html
   */
  public async overlapMetrics(): Promise<OverlapMetricsResponse> {
    return this.httpHandler.get("/monitoring/v1/overlapMetrics");
  }
}
