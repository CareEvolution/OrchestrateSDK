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
  "Argonaut",
  "C4BBClaimCareTeamRole",
  "C4BBClaimDiagnosisType",
  "C4BBCompoundLiteral",
  "CareEvolution",
  "CARIN-BB-Claim-Type",
  "CARIN-BB-DiagnosisType",
  "CdcRaceAndEthnicity",
  "ClaimCareTeamRoleCodes",
  "CMSRemittanceAdviceRemarkCodes",
  "DRG-FY2018",
  "DRG-FY2019",
  "DRG-FY2020",
  "DRG-FY2021",
  "DRG-FY2022",
  "DRG-FY2023",
  "fhir-address-use",
  "fhir-administrative-gender",
  "fhir-allergy-clinical-status",
  "fhir-allergy-intolerance-category",
  "Fhir-allergy-intolerance-category-dstu2",
  "fhir-allergy-intolerance-criticality",
  "fhir-allergy-intolerance-criticality-dstu2",
  "fhir-allergy-intolerance-status",
  "fhir-allergy-intolerance-type",
  "fhir-allergy-verification-status",
  "fhir-allergyintolerance-clinical",
  "fhir-allergyintolerance-verification",
  "fhir-care-plan-activity-status",
  "fhir-claim-type-link",
  "fhir-condition-category",
  "fhir-condition-category-dstu2",
  "fhir-condition-category-stu3",
  "fhir-condition-clinical",
  "fhir-condition-ver-status",
  "fhir-contact-point-system",
  "fhir-contact-point-system-DSTU2",
  "fhir-contact-point-use",
  "fhir-diagnosis-role",
  "fhir-diagnostic-order-priority",
  "fhir-diagnostic-order-status",
  "fhir-diagnostic-report-status",
  "fhir-document-reference-status",
  "fhir-encounter-admit-source",
  "fhir-encounter-class",
  "fhir-event-status",
  "fhir-explanationofbenefit-status",
  "fhir-fm-status",
  "fhir-goal-status",
  "fhir-goal-status-dstu2",
  "fhir-goal-status-stu3",
  "fhir-medication-admin-status",
  "fhir-medication-admin-status-R4",
  "fhir-medication-dispense-status",
  "fhir-medication-order-status",
  "fhir-medication-request-priority",
  "fhir-medication-request-status",
  "fhir-medication-statement-status",
  "fhir-medicationdispense-status",
  "fhir-medicationrequest-status",
  "fhir-name-use",
  "fhir-observation-status",
  "fhir-procedure-request-priority",
  "fhir-procedure-request-status",
  "fhir-reaction-event-severity",
  "fhir-referralstatus",
  "fhir-request-intent",
  "fhir-request-priority",
  "fhir-request-status",
  "fhir-task-intent",
  "fhir-task-status",
  "FhirCodes",
  "FhirCodesAlternate1",
  "FhirCodesAlternate2",
  "FhirCodesAlternate3",
  "FhirCodesAlternate4",
  "FhirCodesAlternate5",
  "FhirCodesAlternate6",
  "FhirCodesAlternate7",
  "HCC-V22",
  "HCC-V23",
  "HCC-V24",
  "HL7 Table 0001 - Administrative Sex",
  "HL7 Table 0002 - Marital Status",
  "HL7 Table 0004 - Patient Class",
  "HL7 Table 0005 - Race",
  "HL7 Table 0006 - Religion",
  "HL7 Table 0189 - Ethnic Group",
  "HL7ActCode",
  "HL7Acuity",
  "HL7ContactInfoUseCode",
  "HL7CurrentSmokingStatus",
  "HL7DetailedEthnicity",
  "HL7Ethnicity",
  "HL7Gender",
  "HL7MaritalStatus",
  "HL7NullFlavor",
  "HL7Race",
  "HL7RaceCategoryExcludingNulls",
  "HL7v3Religion",
  "ICD-9-CM (diagnosis codes)",
  "ICD-9-CM (procedure codes)",
  "InternetSocietyLanguage",
  "NCPDPDispensedAsWrittenOrProductSelectionCode",
  "OMOP",
  "POS",
  "ProviderTaxonomy",
  "Source Of Payment Typology",
  "UCUM",
  "UNII",
  "uscore-condition-category",
  "v2 Name Type",
  "X12ClaimAdjustmentReasonCodes",
] as const;

export type GetFhirR4CodeSystemRequest = {
  codeSystem: typeof codeSystems[number];
  conceptContains?: string;
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

export type GetFhirR4ValueSetsByScopeRequest = {
  name?: string;
  scope?: string;
  pageNumber?: number;
  pageSize?: number;
};

export type GetFhirR4ValueSetsByScopeResponse = Bundle<ValueSet>;
