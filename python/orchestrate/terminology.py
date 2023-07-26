from typing import Literal, TypedDict

from orchestrate._internal.fhir import (
    Bundle,
    CodeSystem,
    CodeableConcept,
    Coding,
    Parameters,
    ValueSet,
)


ClassifyConditionSystems = Literal[
    "http://snomed.info/sct",
    "http://hl7.org/fhir/sid/icd-10-cm",
    "http://hl7.org/fhir/sid/icd-9-cm-diagnosis",
    "ICD-10-CM",
    "ICD-9-CM-Diagnosis",
    "SNOMED",
]

Covid19Condition = Literal[
    "Confirmed",
    "Suspected",
    "Exposure",
    "Encounter",
    "SignsAndSymptoms",
    "NonspecificRespiratoryViralInfection",
]


class ClassifyConditionResponse(TypedDict):
    ccsrCatgory: CodeableConcept
    ccsrDefaultInpatient: Coding
    ccsrDefaultOutpatient: Coding
    cciChronic: bool
    cciAcute: bool
    hccCategory: CodeableConcept
    behavioral: bool
    substance: bool
    socialDeterminant: bool
    covid19Condition: Covid19Condition


ClassifyMedicationSystems = Literal[
    "RxNorm",
    "NDC",
    "CVX",
    "SNOMED",
    "http://www.nlm.nih.gov/research/umls/rxnorm",
    "http://hl7.org/fhir/sid/ndc",
    "http://hl7.org/fhir/sid/cvx",
    "http://snomed.info/sct",
]

Covid19Rx = Literal[
    "vaccination",
    "immunoglobulin",
    "medication",
]


class ClassifyMedicationResponse(TypedDict):
    medRtTherapeuticClass: list[str]
    rxNormIngredient: list[str]
    rxNormStrength: str
    rxNormGeneric: bool
    covid19Rx: Covid19Rx


ClassifyObservationSystems = Literal[
    "http://loinc.org",
    "LOINC",
    "http://snomed.info/sct",
    "SNOMED",
]


class ClassifyObservationResponse(TypedDict):
    loincComponent: str
    loincClass: str
    loincSystem: str
    loincMethodType: str
    loincTimeAspect: str
    covid19Lab: Literal[
        "antigen",
        "antibody",
        "immunoglobulin",
    ]
    category: Literal[
        "activity",
        "exam",
        "imaging",
        "laboratory",
        "procedure",
        "social-history",
        "survey",
        "therapy",
        "vital-signs",
    ]


StandardizeTargetSystems = Literal[
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
    # TODO: "http://www.ama-assn.org/go/cpt-hcpcs" HCPCS URL
    "http://hl7.org/fhir/sid/ndc",
    "http://hl7.org/fhir/sid/cvx",
]

StandardizeResponseSystems = Literal[
    "http://hl7.org/fhir/sid/icd-10",
    "http://hl7.org/fhir/sid/icd-9",
    "http://snomed.info/sct",
    "http://hl7.org/fhir/sid/ndc",
    "http://hl7.org/fhir/sid/cvx",
    "http://www.nlm.nih.gov/research/umls/rxnorm",
    "http://loinc.org",
]


class StandardizeResponseCoding(TypedDict):
    system: StandardizeResponseSystems
    code: str
    display: str


class StandardizeResponse(TypedDict):
    coding: list[StandardizeResponseCoding]


StandardizeConditionResponse = StandardizeResponse

StandardizeMedicationResponse = StandardizeResponse

StandardizeObservationResponse = StandardizeResponse

StandardizeProcedureResponse = StandardizeResponse

StandardizeLabResponse = StandardizeResponse

StandardizeRadiologyResponse = StandardizeResponse

CodeSystems = Literal[
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
]

GetFhirR4CodeSystemResponse = CodeSystem


class _CodeSystemBundleEntry(TypedDict):
    resource: CodeSystem


class _CodeSystemBundle(TypedDict):
    id: str
    resourceType: Literal["Bundle"]
    entry: list[_CodeSystemBundleEntry]


SummarizeFhirR4CodeSystemsResponse = _CodeSystemBundle

TranslateFhirR4ConceptMapResponse = Parameters

TranslateDomains = Literal[
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
]


class _ValueSetBundleEntry(TypedDict):
    resource: ValueSet


class _ValueSetBundle(TypedDict):
    id: str
    resourceType: Literal["Bundle"]
    entry: list[_ValueSetBundleEntry]


SummarizeFhirR4ValueSetScopeResponse = _ValueSetBundle

GetFhirR4ValueSetResponse = ValueSet

SummarizeFhirR4ValueSetResponse = ValueSet

GetFhirR4ValueSetScopesResponse = ValueSet

GetFhirR4ValueSetsByScopeResponse = _ValueSetBundle

SummarizeFhirR4CodeSystemResponse = CodeSystem

GetAllFhirR4ValueSetsForCodesResponse = Parameters

ConvertCombinedFhirR4BundlesResponse = Bundle
