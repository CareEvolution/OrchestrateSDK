import { Bundle, MeasureReport, Measure, Patient, RiskAssessment, OperationOutcome } from "fhir/r4";

const raSegments = [
  "community nondual aged",
  "community full benefit dual aged",
  "community full benefit dual disabled",
  "community nondual disabled",
  "long term institutional",
] as const;

const hccVersions = [
  "22",
  "23",
  "24",
] as const;

export type InsightRiskProfileRequest = {
  content: Bundle;
  hccVersion?: typeof hccVersions[number];
  periodEndDate?: string;
  raSegment?: typeof raSegments[number];
};

export type InsightRiskProfileResource = Patient | MeasureReport | Measure | RiskAssessment | OperationOutcome;

export type InsightRiskProfileResponse = Bundle<InsightRiskProfileResource>;
