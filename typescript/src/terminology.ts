import { Bundle, CodeSystem, CodeableConcept, Coding, ConceptMap, Parameters, ParametersParameter, ValueSet } from "fhir/r4";
import { IHttpHandler } from "./httpHandler";
import { handleBatchOverload } from "./batch";

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

export type GetAllFhirR4ValueSetsForCodesRequest = ClassifyFhirR4ValueSetMembershipRequest;
export type GetAllFhirR4ValueSetsForCodesResponse = ClassifyFhirR4ValueSetMembershipResponse;

export class TerminologyApi {
  private httpHandler: IHttpHandler;

  constructor(httpHandler: IHttpHandler) {
    this.httpHandler = httpHandler;
  }

  handleBatchOverload<TIn, TOut>(url: string, request: TIn): Promise<TOut> {
    return handleBatchOverload<TIn, TOut>(this.httpHandler, url, request);
  }

  /**
   * Classifies a condition, problem, or diagnosis. The input must be from one of the following code systems:
   *
   * - ICD-10-CM
   * - ICD-9-CM-Diagnosis
   * - SNOMED
   * @param request A FHIR Coding
   * @returns A set of key/value pairs representing different classification of the supplied coding
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/condition.html
  */
  classifyCondition(request: ClassifyConditionRequest): Promise<ClassifyConditionResponse>;
  /**
   * Classifies conditions, problems, or diagnoses. The input must be from one of the following code systems:
   * - ICD-10-CM
   * - ICD-9-CM-Diagnosis
   * - SNOMED
   * @param request An array of FHIR Codings
   * @returns An array of sets of key/value pairs representing different classification of the supplied coding in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/condition.html
   */
  classifyCondition(request: ClassifyConditionRequest[]): Promise<ClassifyConditionResponse[]>;
  classifyCondition(request: ClassifyConditionRequest | ClassifyConditionRequest[]): Promise<ClassifyConditionResponse | ClassifyConditionResponse[]> {
    return this.handleBatchOverload("/terminology/v1/classify/condition", request);
  }

  /**
   * Classifies a medication. The input must be from one of the following code systems:
   *
   * - RxNorm
   * - NDC
   * - CVX
   * - SNOMED
   * @param request A FHIR Coding
   * @returns A set of key/value pairs representing different classification of the supplied coding
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html
   */
  classifyMedication(request: ClassifyMedicationRequest): Promise<ClassifyMedicationResponse>;
  /**
   * Classifies medications. The input must be from one of the following code systems:
   *
   * - RxNorm
   * - NDC
   * - CVX
   * - SNOMED
   * @param request An array of FHIR Codings
   * @returns An array of sets of key/value pairs representing different classification of the supplied coding in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html
   */
  classifyMedication(request: ClassifyMedicationRequest[]): Promise<ClassifyMedicationResponse[]>;
  classifyMedication(request: ClassifyMedicationRequest | ClassifyMedicationRequest[]): Promise<ClassifyMedicationResponse | ClassifyMedicationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/classify/medication", request);
  }

  /**
   * Classifies an observation, including lab observations and panels, radiology or other reports. The input must be from one of the following code systems:
   *
   * - LOINC
   * - SNOMED
   * @param request A FHIR Coding
   * @returns A set of key/value pairs representing different classification of the supplied coding
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/observation.html
   */
  classifyObservation(request: ClassifyObservationRequest): Promise<ClassifyObservationResponse>;
  /**
   * Classifies observations, including lab observations and panels, radiology or other reports. The input must be from one of the following code systems:
   *
   * - LOINC
   * - SNOMED
   * @param request An array of FHIR Codings
   * @returns An array of sets of key/value pairs representing different classification of the supplied coding in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/classify/observation.html
   */
  classifyObservation(request: ClassifyObservationRequest[]): Promise<ClassifyObservationResponse[]>;
  classifyObservation(request: ClassifyObservationRequest | ClassifyObservationRequest[]): Promise<ClassifyObservationResponse | ClassifyObservationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/classify/observation", request);
  }

  /**
   * Standardize a condition, problem, or diagnosis
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/condition.html
   */
  standardizeCondition(request: StandardizeRequest): Promise<StandardizeConditionResponse>;
  /**
   * Standardize conditions, problems, or diagnoses
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/condition.html
   */
  standardizeCondition(request: StandardizeRequest[]): Promise<StandardizeConditionResponse[]>;
  standardizeCondition(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeConditionResponse | StandardizeConditionResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/condition", request);
  }

  /**
   * Standardize a medication code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/medication.html
   */
  standardizeMedication(request: StandardizeRequest): Promise<StandardizeMedicationResponse>;
  /**
   * Standardize medication codes
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/medication.html
   */
  standardizeMedication(request: StandardizeRequest[]): Promise<StandardizeMedicationResponse[]>;
  standardizeMedication(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeMedicationResponse | StandardizeMedicationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/medication", request);
  }

  /**
   * Standardize an observation code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/observation.html
   */
  standardizeObservation(request: StandardizeRequest): Promise<StandardizeObservationResponse>;
  /**
   * Standardize observation codes
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/observation.html
   */
  standardizeObservation(request: StandardizeRequest[]): Promise<StandardizeObservationResponse[]>;
  standardizeObservation(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeObservationResponse | StandardizeObservationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/observation", request);
  }

  /**
   * Standardize a procedure
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/procedure.html
   */
  standardizeProcedure(request: StandardizeRequest): Promise<StandardizeObservationResponse>;
  /**
   * Standardize procedures
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/procedure.html
   */
  standardizeProcedure(request: StandardizeRequest[]): Promise<StandardizeObservationResponse[]>;
  standardizeProcedure(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeObservationResponse | StandardizeObservationResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/procedure", request);
  }

  /**
   * Standardize a lab observation or report code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/lab.html
   */
  standardizeLab(request: StandardizeRequest): Promise<StandardizeLabResponse>;
  /**
   * Standardize lab observations or report codes
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/lab.html
   */
  standardizeLab(request: StandardizeRequest[]): Promise<StandardizeLabResponse[]>;
  standardizeLab(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeLabResponse | StandardizeLabResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/lab", request);
  }

  /**
   * Standardize a radiology or other report code
   * @param request A FHIR Coding
   * @returns A collection of standardized codes
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/radiology.html
   */
  standardizeRadiology(request: StandardizeRequest): Promise<StandardizeRadiologyResponse>;
  /**
   * Standardize radiology or other report codes
   * @param request An array of FHIR Codings
   * @returns An array of collections of standardized codes in the same order as the input
   * @link https://rosetta-api.docs.careevolution.com/terminology/standardize/radiology.html
   */
  standardizeRadiology(request: StandardizeRequest[]): Promise<StandardizeRadiologyResponse[]>;
  standardizeRadiology(request: StandardizeRequest | StandardizeRequest[]): Promise<StandardizeRadiologyResponse | StandardizeRadiologyResponse[]> {
    return this.handleBatchOverload("/terminology/v1/standardize/radiology", request);
  }

  /**
   * Describes a code system
   * @param request A code system name
   * @returns A populated CodeSystem
   * @link https://rosetta-api.docs.careevolution.com/fhir/codesystem.html
   */
  getFhirR4CodeSystem(request: GetFhirR4CodeSystemRequest): Promise<GetFhirR4CodeSystemResponse> {
    const urlParameters = new URLSearchParams();
    if (request.pageNumber) {
      urlParameters.append("page.num", request.pageNumber.toString());
    }
    if (request.pageSize) {
      urlParameters.append("_count", request.pageSize.toString());
    }
    if (request.conceptContains) {
      urlParameters.append("concept:contains", request.conceptContains);
    }
    let route = `/terminology/v1/fhir/r4/codesystem/${request.codeSystem}`;
    const urlParametersString = urlParameters.toString();
    if (urlParametersString) {
      route += `?${urlParametersString}`;
    }
    return this.httpHandler.get(route);
  }

  /**
   * Describes available code systems
   * @returns A bundle of known CodeSystems
   * @link https://rosetta-api.docs.careevolution.com/fhir/codesystem.html
   */
  summarizeFhirR4CodeSystems(): Promise<SummarizeFhirR4CodeSystemsResponse> {
    return this.httpHandler.get("/terminology/v1/fhir/r4/codesystem?_summary=true");
  }

  /**
   * Describes available concept maps
   * @returns A bundle of known ConceptMaps
   * @link https://rosetta-api.docs.careevolution.com/fhir/conceptmap.html
   */
  getFhirR4ConceptMaps(): Promise<GetFhirR4ConceptMapResponse> {
    return this.httpHandler.get("/terminology/v1/fhir/r4/conceptmap");
  }

  /**
   * Standardizes source codings to a reference code
   * @param request The best source description of the concept
   * @returns A Parameters object with the `"result"` parameter of `"valueBoolean": true` indicating if the service was able to standardize the code
   * @link https://rosetta-api.docs.careevolution.com/fhir/conceptmap.html
   */
  translateFhirR4ConceptMap(request: TranslateFhirR4ConceptMapRequest): Promise<TranslateFhirR4ConceptMapResponse> {
    let route = "/terminology/v1/fhir/r4/conceptmap/$translate";
    const urlParameters = new URLSearchParams({ code: request.code });
    if (request.domain) {
      urlParameters.append("domain", request.domain);
    }
    route += `?${urlParameters.toString()}`;
    return this.httpHandler.get(route);
  }

  /**
   * Retrieves the set of ValueSets described in a scope
   * @param request A scope identifier
   * @returns A bundle of ValueSets within the requested scope
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  summarizeFhirR4ValueSetScope(request: SummarizeFhirR4ValueSetScopeRequest): Promise<SummarizeFhirR4ValueSetScopeResponse> {
    const params = new URLSearchParams({
      "extension.scope": request.scope,
      _summary: "true"
    });
    const route = `/terminology/v1/fhir/r4/valueset?${params.toString()}`;
    return this.httpHandler.get(route);
  }

  /**
   * Summarizes the total number of codes in a ValueSet
   * @param request A ValueSet identifier
   * @returns A ValueSet resource with only the count populated
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  summarizeFhirR4ValueSet(request: SummarizeFhirR4ValueSetRequest): Promise<SummarizeFhirR4ValueSetResponse> {
    const parameters = new URLSearchParams({
      _summary: "true"
    });
    const route = `/terminology/v1/fhir/r4/valueset/${encodeURIComponent(request.id)}?${parameters.toString()}`;
    return this.httpHandler.get(route);
  }

  /**
   * Retrieves a ValueSet by identifier
   * @param request A ValueSet identifier
   * @returns A ValueSet resource
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  getFhirR4ValueSet(request: GetFhirR4ValueSetRequest): Promise<GetFhirR4ValueSetResponse> {
    const route = `/terminology/v1/fhir/r4/valueset/${encodeURIComponent(request.id)}`;
    return this.httpHandler.get(route);
  }

  /**
   * Retrieves a paginated list of ValueSets filtered by name or scope
   * @param request A paginated request for ValueSets
   * @returns A bundle of ValueSets that match the search criteria
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  getFhirR4ValueSetsByScope(request: GetFhirR4ValueSetsByScopeRequest): Promise<GetFhirR4ValueSetsByScopeResponse> {
    const parameters = new URLSearchParams();
    if (request.name) {
      parameters.append("name", request.name);
    }
    if (request.pageNumber) {
      parameters.append("page.num", request.pageNumber.toString());
    }
    if (request.pageSize) {
      parameters.append("_count", request.pageSize.toString());
    }
    if (request.scope) {
      parameters.append("extension.scope", request.scope);
    }
    const route = `/terminology/v1/fhir/r4/valueset?${parameters.toString()}`;
    return this.httpHandler.get(route);
  }

  /**
   * Requests the available ValueSet scopes
   * @returns A unique ValueSet that contains a list of all scopes available on the server
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  getFhirR4ValueSetScopes(): Promise<GetFhirR4ValueSetScopesResponse> {
    return this.httpHandler.get("/terminology/v1/fhir/r4/valueset/Rosetta.ValueSetScopes");
  }

  /**
   * In some situations it is useful to get the ValueSet(s) that a list of codes are members of. This can be used to categorize or group codes by ValueSet membership. For example, you may wish to:
   *
   *  - Categorize a collection of NDC drug codes by their active ingredient.
   *  - Categorize a collection of LOINC lab tests by the component they are measuring.
   *  - Categorize a collection of ICD-10-CM Diagnoses into a broad set of disease groupings.
   * @param request A Parameters resource containing codes to classify
   * @returns A Parameters resource containing the classification results
   * @link https://rosetta-api.docs.careevolution.com/fhir/valueset.html
   */
  getAllFhirR4ValueSetsForCodes(request: GetAllFhirR4ValueSetsForCodesRequest): Promise<GetAllFhirR4ValueSetsForCodesResponse> {
    const route = "/terminology/v1/fhir/r4/valueset/$classify";
    return this.httpHandler.post(route, request);
  }

  /**
   * Summarizes a code system, typically used to determine number of codes
   * @param request A code system name
   * @returns An unpopulated CodeSystem
   * @link https://rosetta-api.docs.careevolution.com/fhir/codesystem.html
   */
  summarizeFhirR4CodeSystem(request: SummarizeFhirR4CodeSystemRequest): Promise<SummarizeFhirR4CodeSystemResponse> {
    const route = `/terminology/v1/fhir/r4/codesystem/${encodeURIComponent(request.codeSystem)}?_summary=true`;
    return this.httpHandler.get(route);
  }

}
