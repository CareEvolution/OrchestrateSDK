import sys
from typing import Any, Callable, Optional, Union, overload
from urllib.parse import quote

from orchestrate._internal.batch import handle_batch_overloaded_request
from orchestrate._internal.fhir import Parameters
from orchestrate._internal.http_handler import HttpHandler

if sys.version_info < (3, 11):
    from typing_extensions import Literal, NotRequired, TypedDict
else:
    from typing import Literal, TypedDict, NotRequired

from orchestrate._internal.fhir import (
    CodeableConcept,
    CodeSystem,
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


class ClassifyConditionRequest(TypedDict):
    code: str
    system: ClassifyConditionSystems
    display: NotRequired[str]


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


class ClassifyMedicationRequest(TypedDict):
    code: str
    system: ClassifyMedicationSystems
    display: NotRequired[str]


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


class ClassifyObservationRequest(TypedDict):
    code: str
    system: ClassifyObservationSystems
    display: NotRequired[str]


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


class StandardizeRequest(TypedDict):
    code: NotRequired[str]
    system: NotRequired[StandardizeTargetSystems]
    display: NotRequired[str]


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


class ConceptMap(TypedDict):
    resourceType: Literal["ConceptMap"]
    id: str
    name: str
    status: Literal["active", "draft", "retired"]
    url: str
    source: str
    target: str
    group: list[dict[str, Any]]


class _ConceptMapBundleEntry(TypedDict):
    resource: ConceptMap


class ConceptMapBundle(TypedDict):
    id: str
    resourceType: Literal["Bundle"]
    entry: list[_ConceptMapBundleEntry]


GetFhirR4ConceptMapsResponse = ConceptMapBundle

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


def _get_pagination_parameters(
    page_number: Optional[int] = None,
    page_size: Optional[int] = None,
) -> dict[str, Optional[str]]:
    parameters = {
        "page.num": str(page_number) if page_number is not None else None,
        "_count": str(page_size) if page_size is not None else None,
    }
    return parameters


class TerminologyApi:
    def __init__(self, http_handler: HttpHandler) -> None:
        self.__http_handler = http_handler

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self.__http_handler.base_url!r})"

    def _handle_batch_overloaded_request(self, *args, **kwargs) -> Callable[[str], Any]:
        return handle_batch_overloaded_request(self.__http_handler, *args, **kwargs)

    @overload
    def classify_condition(
        self,
        code: str,
        system: ClassifyConditionSystems,
        display: Optional[str] = None,
    ) -> ClassifyConditionResponse:
        """
        Classifies a condition, problem, or diagnosis. The input must be from
        one of the following code systems:

        - ICD-10-CM
        - ICD-9-CM-Diagnosis
        - SNOMED

        ### Parameters

        - `code`: The code of the condition, problem, or diagnosis
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding's code

        ### Returns

        A set of key/value pairs representing different classification of the supplied coding

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/condition.html>
        """
        ...

    @overload
    def classify_condition(
        self, request: ClassifyConditionRequest
    ) -> ClassifyConditionResponse:
        """
        Classifies a condition, problem, or diagnosis. The input must be from
        one of the following code systems:

        - ICD-10-CM
        - ICD-9-CM-Diagnosis
        - SNOMED

        ### Parameters

        - `request`: The `ClassifyConditionRequest`, containing the code, system, and display

        ### Returns

        A set of key/value pairs representing different classification of the supplied coding

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/condition.html>
        """
        ...

    @overload
    def classify_condition(
        self, request: list[ClassifyConditionRequest]
    ) -> list[ClassifyConditionResponse]:
        """
        Classifies conditions, problems, or diagnoses. The input must be from
        one of the following code systems:

        - ICD-10-CM
        - ICD-9-CM-Diagnosis
        - SNOMED

        ### Parameters

        - `request`: A list of `ClassifyConditionRequest`, containing the code, system, and display

        ### Returns

        A list of sets of key/value pairs representing different classification of the supplied coding
        in the same order as the input list.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/condition.html>
        """
        ...

    def classify_condition(
        self, *args, **kwargs
    ) -> Union[ClassifyConditionResponse, list[ClassifyConditionResponse]]:
        url = "/terminology/v1/classify/condition"
        overload_handler = self._handle_batch_overloaded_request(*args, **kwargs)
        return overload_handler(url)

    @overload
    def classify_medication(
        self,
        code: str,
        system: ClassifyMedicationSystems,
        display: Optional[str] = None,
    ) -> ClassifyMedicationResponse:
        """
        Classifies a medication. The input must be from one of the following code systems:

        - RxNorm
        - NDC
        - CVX
        - SNOMED

        ### Parameters

        - `code`: The code of the medication
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A set of key/value pairs representing different classification of the supplied coding

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html>
        """
        ...

    @overload
    def classify_medication(
        self, request: ClassifyMedicationRequest
    ) -> ClassifyMedicationResponse:
        """
        Classifies a medication. The input must be from one of the following code systems:

        - RxNorm
        - NDC
        - CVX
        - SNOMED

        ### Parameters

        - `request`: The `ClassifyMedicationRequest`, containing the code, system, and display

        ### Returns

        A set of key/value pairs representing different classification of the supplied coding

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html>
        """
        ...

    @overload
    def classify_medication(
        self, request: list[ClassifyMedicationRequest]
    ) -> list[ClassifyMedicationResponse]:
        """
        Classifies medications. The input must be from one of the following code systems:

        - RxNorm
        - NDC
        - CVX
        - SNOMED

        ### Parameters

        - `request`: A list of `ClassifyMedicationRequest`, containing the code, system, and display

        ### Returns

        A list of sets of key/value pairs representing different classification of the supplied coding
        in the same order as the input list.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html>
        """
        ...

    def classify_medication(
        self, *args, **kwargs
    ) -> Union[ClassifyMedicationResponse, list[ClassifyMedicationResponse]]:
        url = "/terminology/v1/classify/medication"
        overload_handler = self._handle_batch_overloaded_request(*args, **kwargs)
        return overload_handler(url)

    @overload
    def classify_observation(
        self,
        code: str,
        system: ClassifyObservationSystems,
        display: Optional[str] = None,
    ) -> ClassifyObservationResponse:
        """
        Classifies an observation, including lab observations and panels,
        radiology or other reports. The input must be from one of the following
        code systems:

        - LOINC
        - SNOMED

        ### Parameters

        - `code`: The code of the observation
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A set of key/value pairs representing different classification of the supplied coding

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/observation.html>
        """
        ...

    @overload
    def classify_observation(
        self, request: ClassifyObservationRequest
    ) -> ClassifyObservationResponse:
        """
        Classifies an observation, including lab observations and panels,
        radiology or other reports. The input must be from one of the following
        code systems:

        - LOINC
        - SNOMED

        ### Parameters

        - `request`: The `ClassifyObservationRequest`, containing the code, system, and display

        ### Returns

        A set of key/value pairs representing different classification of the supplied coding

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/observation.html>
        """
        ...

    @overload
    def classify_observation(
        self, request: list[ClassifyObservationRequest]
    ) -> list[ClassifyObservationResponse]:
        """
        Classifies observations, including lab observations and panels,
        radiology or other reports. The input must be from one of the following
        code systems:

        - LOINC
        - SNOMED

        ### Parameters

        - `request`: A list of `ClassifyObservationRequest`, containing the code, system, and display

        ### Returns

        A list of sets of key/value pairs representing different classification of the supplied coding

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/observation.html>
        """
        ...

    def classify_observation(
        self, *args, **kwargs
    ) -> Union[ClassifyObservationResponse, list[ClassifyObservationResponse]]:
        url = "/terminology/v1/classify/observation"
        overload_handler = self._handle_batch_overloaded_request(*args, **kwargs)
        return overload_handler(url)

    @overload
    def standardize_condition(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeConditionResponse:
        """
        Standardize a condition, problem, or diagnosis

        ### Parameters

        - `code`: The code of the condition, problem, or diagnosis
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding's code

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/condition.html>
        """
        ...

    @overload
    def standardize_condition(
        self, request: StandardizeRequest
    ) -> StandardizeConditionResponse:
        """
        Standardize a condition, problem, or diagnosis

        ### Parameters

        - `request`: The `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/condition.html>
        """
        ...

    @overload
    def standardize_condition(
        self, request: list[StandardizeRequest]
    ) -> list[StandardizeConditionResponse]:
        """
        Standardize conditions, problems, or diagnoses

        ### Parameters

        - `request`: A list of `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/condition.html>
        """
        ...

    def standardize_condition(
        self, *args, **kwargs
    ) -> Union[StandardizeConditionResponse, list[StandardizeConditionResponse]]:
        url = "/terminology/v1/standardize/condition"
        overload_handler = self._handle_batch_overloaded_request(*args, **kwargs)
        return overload_handler(url)

    @overload
    def standardize_medication(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeMedicationResponse:
        """
        Standardize a medication code

        ### Parameters

        - `code`: The code of the medication
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html>
        """
        ...

    @overload
    def standardize_medication(
        self, request: StandardizeRequest
    ) -> StandardizeMedicationResponse:
        """
        Standardize a medication code

        ### Parameters

        - `request`: The `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html>
        """
        ...

    @overload
    def standardize_medication(
        self, request: list[StandardizeRequest]
    ) -> list[StandardizeMedicationResponse]:
        """
        Standardize medication codes

        ### Parameters

        - `request`: A list of `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A list of collections of standardized codes in the same order as the input list.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/classify/medication.html>
        """
        ...

    def standardize_medication(
        self, *args, **kwargs
    ) -> Union[StandardizeMedicationResponse, list[StandardizeMedicationResponse]]:
        url = "/terminology/v1/standardize/medication"
        overload_handler = self._handle_batch_overloaded_request(*args, **kwargs)
        return overload_handler(url)

    @overload
    def standardize_observation(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeObservationResponse:
        """
        Standardize an observation code

        ### Parameters

        - `code`: The code of the observation
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/observation.html>
        """
        ...

    @overload
    def standardize_observation(
        self,
        request: StandardizeRequest,
    ) -> StandardizeObservationResponse:
        """
        Standardize an observation code

        ### Parameters

        - `request`: The `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/observation.html>
        """
        ...

    @overload
    def standardize_observation(
        self,
        request: list[StandardizeRequest],
    ) -> list[StandardizeObservationResponse]:
        """
        Standardize observation codes

        ### Parameters

        - `request`: A list of `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A list of collections of standardized codes in the same order as the input list.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/observation.html>
        """
        ...

    def standardize_observation(
        self, *args, **kwargs
    ) -> Union[StandardizeObservationResponse, list[StandardizeObservationResponse]]:
        url = "/terminology/v1/standardize/observation"
        overload_handler = self._handle_batch_overloaded_request(*args, **kwargs)
        return overload_handler(url)

    @overload
    def standardize_procedure(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeProcedureResponse:
        """
        Standardize a procedure code

        ### Parameters

        - `code`: The code of the procedure
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/procedure.html>
        """
        ...

    @overload
    def standardize_procedure(
        self,
        request: StandardizeRequest,
    ) -> StandardizeProcedureResponse:
        """
        Standardize a procedure code

        ### Parameters

        - `request`: The `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/procedure.html>
        """
        ...

    @overload
    def standardize_procedure(
        self,
        request: list[StandardizeRequest],
    ) -> list[StandardizeProcedureResponse]:
        """
        Standardize procedure codes

        ### Parameters

        - `request`: A list of `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A list of collections of standardized codes in the same order as the input list.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/procedure.html>
        """
        ...

    def standardize_procedure(
        self, *args, **kwargs
    ) -> Union[StandardizeProcedureResponse, list[StandardizeProcedureResponse]]:
        url = "/terminology/v1/standardize/procedure"
        overload_handler = self._handle_batch_overloaded_request(*args, **kwargs)
        return overload_handler(url)

    @overload
    def standardize_lab(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeLabResponse:
        """
        Standardize a lab code

        ### Parameters

        - `code`: The code of the lab
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/lab.html>
        """
        ...

    @overload
    def standardize_lab(
        self,
        request: StandardizeRequest,
    ) -> StandardizeLabResponse:
        """
        Standardize a lab code

        ### Parameters

        - `request`: The `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/lab.html>
        """
        ...

    @overload
    def standardize_lab(
        self,
        request: list[StandardizeRequest],
    ) -> list[StandardizeLabResponse]:
        """
        Standardize lab codes

        ### Parameters

        - `request`: A list of `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A list of collections of standardized codes in the same order as the input list.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/lab.html>
        """
        ...

    def standardize_lab(
        self, *args, **kwargs
    ) -> Union[StandardizeLabResponse, list[StandardizeLabResponse]]:
        url = "/terminology/v1/standardize/lab"
        overload_handler = self._handle_batch_overloaded_request(*args, **kwargs)
        return overload_handler(url)

    @overload
    def standardize_radiology(
        self,
        code: Optional[str] = None,
        system: Optional[StandardizeTargetSystems] = None,
        display: Optional[str] = None,
    ) -> StandardizeRadiologyResponse:
        """
        Standardize a radiology code

        ### Parameters

        - `code`: The code of the radiology
        - `system`: The system of the Coding's code
        - `display`: The display of the Coding

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/radiology.html>
        """
        ...

    @overload
    def standardize_radiology(
        self,
        request: StandardizeRequest,
    ) -> StandardizeRadiologyResponse:
        """
        Standardize a radiology code

        ### Parameters

        - `request`: The `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A collection of standardized codes

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/radiology.html>
        """
        ...

    @overload
    def standardize_radiology(
        self,
        request: list[StandardizeRequest],
    ) -> list[StandardizeRadiologyResponse]:
        """
        Standardize radiology codes

        ### Parameters

        - `request`: A list of `StandardizeRequest`, containing the code, system, and display

        ### Returns

        A list of collections of standardized codes in the same order as the input list.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/terminology/standardize/radiology.html>
        """
        ...

    def standardize_radiology(
        self, *args, **kwargs
    ) -> Union[StandardizeRadiologyResponse, list[StandardizeRadiologyResponse]]:
        url = "/terminology/v1/standardize/radiology"
        overload_handler = self._handle_batch_overloaded_request(*args, **kwargs)
        return overload_handler(url)

    def get_fhir_r4_code_system(
        self,
        code_system: CodeSystems,
        concept_contains: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> GetFhirR4CodeSystemResponse:
        """
        Describes a code system

        ### Parameters

        - `code_system`: The CodeSystem to retrieve
        - `page_number`: When paginating, the page number to retrieve
        - `page_size`: When paginating, The page size to retrieve

        ### Returns

        A FHIR R4 CodeSystem resource

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/codesystem.html>
        """
        parameters = _get_pagination_parameters(page_number, page_size)
        if concept_contains is not None:
            parameters["concept:contains"] = concept_contains

        return self.__http_handler.get(
            path=f"/terminology/v1/fhir/r4/codesystem/{code_system}",
            parameters=parameters,
        )

    def summarize_fhir_r4_code_systems(self) -> SummarizeFhirR4CodeSystemsResponse:
        """
        Describes available code systems

        ### Returns

        A bundle of known CodeSystems

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/codesystem.html>
        """
        return self.__http_handler.get(
            path="/terminology/v1/fhir/r4/codesystem", parameters={"_summary": "true"}
        )

    def get_fhir_r4_concept_maps(
        self,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> GetFhirR4ConceptMapsResponse:
        """
        Describes available concept maps

        ### Returns

        A bundle of known ConceptMaps

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/conceptmap.html>
        """
        return self.__http_handler.get(path=f"/terminology/v1/fhir/r4/conceptmap")

    def translate_fhir_r4_concept_map(
        self,
        code: str,
        domain: Optional[TranslateDomains] = None,
    ) -> TranslateFhirR4ConceptMapResponse:
        """
        Standardizes source codings to a reference code

        ### Parameters

        - `code`: The code of the condition, problem, or diagnosis
        - `domain`: The source domain of the code

        ### Returns

        A Parameters object with the `"result"` parameter of `"valueBoolean": true` indicating if the service was able to standardize the code

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/conceptmap.html>
        """
        parameters = {
            "code": code,
            "domain": domain,
        }
        return self.__http_handler.get(
            path="/terminology/v1/fhir/r4/conceptmap/$translate",
            parameters=parameters,
        )

    def summarize_fhir_r4_value_set_scope(
        self, scope: str
    ) -> SummarizeFhirR4ValueSetScopeResponse:
        """
        Retrieves the set of ValueSets described in a scope

        ### Parameters

        - `scope`: The scope identifier

        ### Returns

        A bundle of ValueSets within the requested scope

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        parameters = {
            "extension.scope": scope,
            "_summary": "true",
        }
        return self.__http_handler.get(
            path="/terminology/v1/fhir/r4/valueset",
            parameters=parameters,
        )

    def get_fhir_r4_value_set(
        self,
        value_set_id: str,
    ) -> GetFhirR4ValueSetResponse:
        """
        Retrieves a ValueSet by identifier

        ### Parameters

        - `value_set_id`: The ValueSet identifier

        ### Returns

        A ValueSet

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        return self.__http_handler.get(
            path=f"/terminology/v1/fhir/r4/valueset/{quote(value_set_id)}",
        )

    def summarize_fhir_r4_value_set(
        self,
        value_set_id: str,
    ) -> SummarizeFhirR4ValueSetResponse:
        """
        Summarizes the total number of codes in a ValueSet

        ### Parameters

        - `value_set_id`: The ValueSet identifier

        ### Returns

        A ValueSet resource with only the count populated

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        return self.__http_handler.get(
            path=f"/terminology/v1/fhir/r4/valueset/{quote(value_set_id)}",
            parameters={"_summary": "true"},
        )

    def get_fhir_r4_value_set_scopes(self) -> GetFhirR4ValueSetScopesResponse:
        """
        Requests the available ValueSet scopes

        ### Returns

        A unique ValueSet that contains a list of all scopes available on the server

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        return self.__http_handler.get(
            path="/terminology/v1/fhir/r4/valueset/Rosetta.ValueSetScopes",
        )

    def get_fhir_r4_value_sets_by_scope(
        self,
        name: Optional[str] = None,
        scope: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> GetFhirR4ValueSetsByScopeResponse:
        """
        Retrieves a paginated list of ValueSets filtered by name or scope

        ### Parameters

        - `name`: The name of the ValueSet
        - `scope`: Scope the ValueSet is in
        - `page_number`: When paginating, the page number to retrieve
        - `page_size`: When paginating, The page size to retrieve

        ### Returns

        A bundle of ValueSets that match the search criteria

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        parameters = {
            **_get_pagination_parameters(page_number, page_size),
            "name": name,
            "extension.scope": scope,
        }
        return self.__http_handler.get(
            path=f"/terminology/v1/fhir/r4/valueset",
            parameters=parameters,
        )

    def summarize_fhir_r4_code_system(
        self, code_system: CodeSystems
    ) -> SummarizeFhirR4CodeSystemResponse:
        """
        Summarizes a code system, typically used to determine number of codes

        ### Parameters

        - `code_system`: The CodeSystem name to retrieve

        ### Returns

        An unpopulated CodeSystem

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/codesystem.html>
        """
        return self.__http_handler.get(
            path=f"/terminology/v1/fhir/r4/codesystem/{code_system}",
            parameters={"_summary": "true"},
        )

    def get_all_fhir_r4_value_sets_for_codes(
        self, parameters: Parameters
    ) -> GetAllFhirR4ValueSetsForCodesResponse:
        """
        In some situations it is useful to get the ValueSet(s) that a list of
        codes are members of. This can be used to categorize or group codes by
        ValueSet membership. For example, you may wish to:

        - Categorize a collection of NDC drug codes by their active ingredient.
        - Categorize a collection of LOINC lab tests by the component they are
          measuring.
        - Categorize a collection of ICD-10-CM Diagnoses into a broad set of
          disease groupings.

        ### Parameters

        - `parameters`: A Parameters resource containing at least one code, a system,
            and optionally a scope

        ### Returns

        A Parameters resource containing the classification results

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/valueset.html>
        """
        return self.__http_handler.post(
            path="/terminology/v1/fhir/r4/valueset/$classify",
            body=parameters,
        )
