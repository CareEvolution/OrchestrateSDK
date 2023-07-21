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
