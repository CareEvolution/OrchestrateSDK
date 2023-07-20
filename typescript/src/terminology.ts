import { Bundle, CodeSystem, CodeableConcept, Coding, ConceptMap, Parameters, ParametersParameter, ValueSet } from "fhir/r4";

const standardizeTargetSystems = [
  "ICD-10-CM",
  "ICD-9-CM-Diagnosis",
  "SNOMED",
  "RxNorm",
  "LOINC",
  "CPT",
  "HCPCS",
  "NDC",
  "CVX",
  "http://hl7.org/fhir/sid/icd-10",
  "http://hl7.org/fhir/sid/icd-9",
  "http://snomed.info/sct",
  "http://www.nlm.nih.gov/research/umls/rxnorm",
  "http://loinc.org",
  "http://www.ama-assn.org/go/cpt",
  // TODO: "http://www.ama-assn.org/go/cpt-hcpcs" HCPCS URL
  "http://hl7.org/fhir/sid/ndc",
  "http://hl7.org/fhir/sid/cvx",
] as const;

const standardizeResponseSystems = [
  "http://hl7.org/fhir/sid/icd-10",
  "http://hl7.org/fhir/sid/icd-9",
  "http://snomed.info/sct",
  "http://hl7.org/fhir/sid/ndc",
  "http://hl7.org/fhir/sid/cvx",
  "http://www.nlm.nih.gov/research/umls/rxnorm",
  "http://loinc.org",
] as const;

export type StandardizeTargetSystem = typeof standardizeTargetSystems[number];

export type StandardizeRequest = Coding & { targetSystem?: StandardizeTargetSystem; };

export type StandardizeResponseCoding = Coding & { system: typeof standardizeResponseSystems[number]; };

export type StandardizeResponse = {
  readonly coding: ReadonlyArray<StandardizeResponseCoding>;
};

export type StandardizeConditionResponse = StandardizeResponse;

export type StandardizeMedicationResponse = StandardizeResponse;

export type StandardizeObservationResponse = StandardizeResponse;

export type StandardizeProcedureResponse = StandardizeResponse;

export type StandardizeLabResponse = StandardizeResponse;

export type StandardizeRadiologyResponse = StandardizeResponse;


export type ClassifyRequest = Coding;


const classifyConditionSystems = [
  "http://snomed.info/sct",
  "http://hl7.org/fhir/sid/icd-10-cm",
  "http://hl7.org/fhir/sid/icd-9-cm-diagnosis",
  "ICD-10-CM",
  "ICD-9-CM-Diagnosis",
  "SNOMED",
] as const;

export type ClassifyConditionSystem = typeof classifyConditionSystems[number];

export type ClassifyConditionRequest = ClassifyRequest & { system: ClassifyConditionSystem; };

const covid19Condition = [
  "Confirmed",
  "Suspected",
  "Exposure",
  "Encounter",
  "SignsAndSymptoms",
  "NonspecificRespiratoryViralInfection",
] as const;

export type ClassifyConditionResponse = {
  ccsrCatgory: CodeableConcept;
  ccsrDefaultInpatient: Coding;
  ccsrDefaultOutpatient: Coding;
  cciChronic: boolean;
  cciAcute: boolean;
  hccCategory: CodeableConcept;
  behavioral: boolean;
  substance: boolean;
  socialDeterminant: boolean;
  covid19Condition: typeof covid19Condition;
};


const classifyMedicationSystems = [
  "RxNorm",
  "NDC",
  "CVX",
  "SNOMED",
  "http://www.nlm.nih.gov/research/umls/rxnorm",
  "http://hl7.org/fhir/sid/ndc",
  "http://hl7.org/fhir/sid/cvx",
  "http://snomed.info/sct",
] as const;

export type ClassifyMedicationSystem = typeof classifyMedicationSystems[number];

export type ClassifyMedicationRequest = ClassifyRequest & { system: ClassifyMedicationSystem; };

const covid19Rx = ["vaccination", "immunoglobulin", "medication"] as const;

export type ClassifyMedicationResponse = {
  medRtTherapeuticClass: string[];
  rxNormIngredient: string[];
  rxNormStrength: string;
  rxNormGeneric: boolean;
  covid19Rx: typeof covid19Rx;
};

const classifyObservationSystems = [
  "http://loinc.org",
  "LOINC",
  "http://snomed.info/sct",
  "SNOMED",
] as const;


export type ClassifyObservationRequest = ClassifyRequest & { system: typeof classifyObservationSystems[number]; };

export type ClassifyObservationResponse = {
  loincComponent: string;
  loincClass: string;
  loincSystem: string;
  loincMethodType: string;
  loincTimeAspect: string;
  covid19Lab: [
    "antigen",
    "antibody",
    "immunoglobulin",
  ];
  category: [
    "activity",
    "exam",
    "imaging",
    "laboratory",
    "procedure",
    "social-history",
    "survey",
    "therapy",
    "vital-signs",
  ];
};

export type GetFhirR4CodeSystemResponse = CodeSystem;

export type SummarizeFhirR4CodeSystemsResponse = Bundle<CodeSystem>;

const codeSystems = [
  "ICD-10-CM",
  "ICD-9-CM-Diagnosis",
  "SNOMED",
  "RxNorm",
  "LOINC",
  "CPT",
  "HCPCS",
  "NDC",
  "CVX",
] as const;

export type GetFhirR4CodeSystemRequest = {
  codeSystem: typeof codeSystems[number];
  pageNumber?: number;
  pageSize?: number;
};

export type SummarizeFhirR4CodeSystemRequest = {
  codeSystem: typeof codeSystems[number];
};

export type SummarizeFhirR4CodeSystemResponse = CodeSystem;

export type GetFhirR4ConceptMapResponse = Bundle<ConceptMap>;

export type TranslateFhirR4ConceptMapResponse = Parameters;

const translateDomains = [
  "Condition",
  "AllergyIntolerance",
  "MedicationDispense",
  "MedicationAdministration",
  "MedicationRequest",
  "ExplanationOfBenefit",
  "Encounter",
  "Procedure",
  "DiagnosticReport",
  "Observation",
  "ServiceRequest",
  "Patient",
  "Practitioner",
  "Person",
  "CarePlan",
] as const;

export type TranslateFhirR4ConceptMapRequest = {
  code: string;
  domain?: typeof translateDomains[number];
};

export type GetFhirR4ValueSetScopesResponse = ValueSet;

export type SummarizeFhirR4ValueSetScopeRequest = {
  scope: string;
};

export type SummarizeFhirR4ValueSetScopeResponse = Bundle<ValueSet>;

export type SummarizeFhirR4ValueSetRequest = {
  id: string;
};

export type SummarizeFhirR4ValueSetResponse = ValueSet;

export type GetFhirR4ValueSetRequest = {
  id: string;
};

export type GetFhirR4ValueSetResponse = ValueSet;

const classifyValueSetSystems = [
  "http://snomed.info/sct",
  "http://hl7.org/fhir/sid/icd-10-cm",
  "http://hl7.org/fhir/sid/icd-9-cm-diagnosis",
  "http://hl7.org/fhir/sid/ndc",
  "http://hl7.org/fhir/sid/cvx",
] as const;

type ClassifyFhirR4ValueSetMembershipRequestSystem = ParametersParameter & {
  name: "system";
  valueString: typeof classifyValueSetSystems[number];
};

type ClassifyFhirR4ValueSetMembershipRequestCode = ParametersParameter & {
  name: "code";
  valueString: string;
};

type ClassifyFhirR4ValueSetMembershipRequestScope = ParametersParameter & {
  name: "scope";
  valueString: string;
};

type ClassifyFhirR4ValueSetMembershipRequestParameter =
  ClassifyFhirR4ValueSetMembershipRequestCode
  | ClassifyFhirR4ValueSetMembershipRequestScope
  | ClassifyFhirR4ValueSetMembershipRequestSystem;

export type ClassifyFhirR4ValueSetMembershipRequest = Parameters & {
  parameter: ClassifyFhirR4ValueSetMembershipRequestParameter[];
};

export type ClassifyFhirR4ValueSetMembershipResponse = Parameters;

export type GetFhirR4ValueSetScopeRequest = {
  scope?: string;
  pageNumber?: number;
  pageSize?: number;
};

export type GetFhirR4ValueSetScopeResponse = Bundle<ValueSet>;
