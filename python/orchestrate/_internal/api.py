import json
from typing import Any, Callable, Literal, Mapping, Optional, Union, overload
from urllib.parse import quote

import requests
from orchestrate.convert import (
    ConvertCdaToFhirR4Response,
    ConvertCdaToPdfResponse,
    ConvertFhirR4ToCdaResponse,
    ConvertFhirR4ToOmopResponse,
    ConvertHl7ToFhirR4Response,
    ConvertX12ToFhirR4Response,
)
from orchestrate._internal.fhir import Bundle, Parameters
from orchestrate.insight import InsightRiskProfileResponse
from orchestrate.terminology import (
    ClassifyConditionRequest,
    ClassifyConditionResponse,
    ClassifyConditionSystems,
    ClassifyMedicationRequest,
    ClassifyMedicationResponse,
    ClassifyMedicationSystems,
    ClassifyObservationRequest,
    ClassifyObservationResponse,
    ClassifyObservationSystems,
    CodeSystems,
    ConvertCombinedFhirR4BundlesResponse,
    GetAllFhirR4ValueSetsForCodesResponse,
    GetFhirR4CodeSystemResponse,
    GetFhirR4ValueSetResponse,
    GetFhirR4ValueSetScopesResponse,
    GetFhirR4ValueSetsByScopeResponse,
    StandardizeConditionResponse,
    StandardizeLabResponse,
    StandardizeMedicationResponse,
    StandardizeObservationResponse,
    StandardizeProcedureResponse,
    StandardizeRadiologyResponse,
    StandardizeRequest,
    StandardizeTargetSystems,
    SummarizeFhirR4CodeSystemResponse,
    SummarizeFhirR4CodeSystemsResponse,
    SummarizeFhirR4ValueSetResponse,
    SummarizeFhirR4ValueSetScopeResponse,
    TranslateDomains,
    TranslateFhirR4ConceptMapResponse,
)


class _RosettaApi:
    def __init__(
        self,
        base_url: str,
        default_headers: dict,
    ) -> None:
        self._base_url = base_url
        self.__default_headers = default_headers

    def __merge_headers(self, headers: Optional[dict]) -> dict:
        if headers is None:
            return self.__default_headers
        return {**self.__default_headers, **headers}

    def _post(
        self,
        path: str,
        body: Any,
        headers: Optional[dict[str, str]] = None,
        parameters: Optional[dict[str, Optional[str]]] = None,
    ) -> Any:
        request_headers = self.__merge_headers(headers)

        prepared_body = (
            json.dumps(body)
            if request_headers["Content-Type"] == "application/json"
            else body
        )
        url = f"{self._base_url}{path}"

        response = requests.post(
            url,
            data=prepared_body,
            headers=request_headers,
            params=parameters,
        )
        response.raise_for_status()

        if (
            request_headers["Accept"] in ["application/zip", "application/pdf"]
        ) and response.content:
            return response.content

        if (request_headers["Accept"] == "application/json") and response.text:
            return response.json()

        return response.text

    def _get(
        self,
        path: str,
        headers: Optional[dict] = None,
        parameters: Optional[Mapping[str, Optional[str]]] = None,
    ) -> Any:
        request_headers = self.__merge_headers(headers)

        url = f"{self._base_url}{path}"
        response = requests.get(
            url,
            headers=request_headers,
            params=parameters,
        )
        response.raise_for_status()

        if (request_headers["Accept"] == "application/json") and response.text:
            return response.json()

        return response.text


def _get_coding_body(
    code: Optional[str] = None,
    system: Optional[str] = None,
    display: Optional[str] = None,
) -> dict[str, str]:
    body = {}
    if code is not None:
        body["code"] = code
    if system is not None:
        body["system"] = system
    if display is not None:
        body["display"] = display

    return body


def _get_pagination_parameters(
    page_number: Optional[int] = None,
    page_size: Optional[int] = None,
) -> dict[str, Optional[str]]:
    parameters = {
        "page.num": str(page_number) if page_number is not None else None,
        "_count": str(page_size) if page_size is not None else None,
    }
    return parameters


def _get_id_dependent_route(
    route: str,
    id_: Optional[str] = None,
) -> str:
    if id_ is not None:
        route += f"/{quote(id_)}"
    return route


class OrchestrateApi(_RosettaApi):
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        additional_headers: Optional[dict] = None,
    ) -> None:
        default_headers = {
            **(additional_headers or {}),
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if api_key is not None:
            default_headers["x-api-key"] = api_key

        super().__init__(
            base_url=base_url or "https://api.rosetta.careevolution.com",
            default_headers=default_headers,
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self._base_url!r})"

    def _handle_batch_overloaded_request(self, *args, **kwargs) -> Callable[[str], Any]:
        body: dict[str, Any] = {}
        request = kwargs.get("request")
        if request is None and len(args) > 0:
            request = args[0]
        if isinstance(request, list):
            body = {"items": [_get_coding_body(**item) for item in request]}
            return lambda url: self._post(f"{url}/batch", body).get("items")
        if isinstance(request, dict):
            body = _get_coding_body(**request)
            return lambda url: self._post(url, body)

        code = kwargs.get("code") or (args[0] if len(args) > 0 else None)
        system = kwargs.get("system") or (args[1] if len(args) > 1 else None)
        display = kwargs.get("display") or (args[2] if len(args) > 2 else None)
        body = _get_coding_body(code, system, display)
        return lambda url: self._post(url, body)

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

    def convert_hl7_to_fhir_r4(
        self,
        content: str,
        patient_id: Optional[str] = None,
    ) -> ConvertHl7ToFhirR4Response:
        """
        Converts one or more HL7v2 messages into a FHIR R4 bundle

        ### Parameters

        - `hl7_message`: The HL7 message(s) to convert
        - `patient_id`: The patient ID to use for the FHIR bundle

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the HL7 messages

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/hl7_to_fhir.html>
        """
        headers = {"Content-Type": "text/plain"}
        route = _get_id_dependent_route("/convert/v1/hl7tofhirr4", patient_id)
        return self._post(
            path=route,
            body=content,
            headers=headers,
        )

    def convert_cda_to_fhir_r4(
        self,
        content: str,
        patient_id: Optional[str] = None,
    ) -> ConvertCdaToFhirR4Response:
        """
        Converts a CDA document into a FHIR R4 bundle

        ### Parameters

        - `cda`: The CDA document to convert
        - `patient_id`: The patient ID to use for the FHIR bundle

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the CDA

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/cda_to_fhir.html>
        """
        headers = {"Content-Type": "application/xml"}
        route = _get_id_dependent_route("/convert/v1/cdatofhirr4", patient_id)
        return self._post(
            path=route,
            body=content,
            headers=headers,
        )

    def convert_cda_to_pdf(self, content: str) -> ConvertCdaToPdfResponse:
        """
        Converts a CDA document into a PDF document

        ### Parameters

        - `cda`: The CDA document to convert

        ### Returns

        A formatted PDF document suitable for human review

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/cda_to_pdf.html>
        """
        headers = {"Content-Type": "application/xml", "Accept": "application/pdf"}
        response = self._post(
            path="/convert/v1/cdatopdf",
            body=content,
            headers=headers,
        )
        return response

    def convert_fhir_r4_to_cda(self, content: Bundle) -> ConvertFhirR4ToCdaResponse:
        """
        Converts a FHIR R4 bundle into an aggregated CDA document.

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient

        ### Returns

        An aggregated C-CDA R2.1 document in XML format

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/fhir_to_cda.html>
        """
        headers = {"Accept": "application/xml"}
        return self._post(
            path="/convert/v1/fhirr4tocda",
            body=content,
            headers=headers,
        )

    def convert_fhir_r4_to_omop(self, content: Bundle) -> ConvertFhirR4ToOmopResponse:
        """
        Converts a FHIR R4 bundle into the OMOP Common Data Model v5.4 format.

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient

        ### Returns

        A ZIP archive containing multiple CSV files, one for each supported OMOP data table.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/fhir_to_omop.html>
        """
        headers = {
            "Accept": "application/zip",
        }
        response = self._post(
            path="/convert/v1/fhirr4toomop",
            body=content,
            headers=headers,
        )
        return response

    def convert_x12_to_fhir_r4(
        self,
        content: str,
        patient_id: Optional[str] = None,
    ) -> ConvertX12ToFhirR4Response:
        """
        Converts an X12 document into a FHIR R4 bundle

        ### Parameters

        - `x12_document`: The X12 document to convert
        - `patient_id`: The patient ID to use for the FHIR bundle

        ### Returns

        A FHIR R4 Bundle containing the clinical data parsed out of the X12
        """
        headers = {"Content-Type": "text/plain"}
        route = _get_id_dependent_route("/convert/v1/x12tofhirr4", patient_id)
        return self._post(
            path=route,
            body=content,
            headers=headers,
        )

    def insight_risk_profile(
        self,
        content: Bundle,
        hcc_version: Optional[Literal["22", "23", "24"]] = None,
        period_end_date: Optional[str] = None,
        ra_segment: Optional[
            Literal[
                "community nondual aged",
                "community full benefit dual aged",
                "community full benefit dual disabled",
                "community nondual disabled",
                "long term institutional",
            ]
        ] = None,
    ) -> InsightRiskProfileResponse:
        """
        Computes an HCC Risk Adjustment Profile for the provided patient

        ### Parameters

        - `fhir_bundle`: A FHIR R4 bundle for a single patient
        - `hcc_version`: The HCC version to use
        - `period_end_date`: The period end date to use
        - `ra_segment`: The risk adjustment segment to use

        ### Returns

        A new FHIR R4 Bundle containing measure and assessment resources

        ### Documentation

        <
        """
        parameters = {
            "hccVersion": hcc_version,
            "periodEndDate": period_end_date,
            "raSegment": ra_segment,
        }
        return self._post(
            path="/insight/v1/riskprofile",
            body=content,
            parameters=parameters,
        )

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

        return self._get(
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
        return self._get(
            path="/terminology/v1/fhir/r4/codesystem", parameters={"_summary": "true"}
        )

    def get_fhir_r4_concept_maps(
        self,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> GetFhirR4CodeSystemResponse:
        """
        Describes available concept maps

        ### Returns

        A bundle of known ConceptMaps

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/fhir/conceptmap.html>
        """
        return self._get(path=f"/terminology/v1/fhir/r4/conceptmap")

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
        return self._get(
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
        return self._get(
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
        return self._get(
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
        return self._get(
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
        return self._get(
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
        return self._get(
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
        return self._get(
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
        return self._post(
            path="/terminology/v1/fhir/r4/valueset/$classify",
            body=parameters,
        )

    def convert_combined_fhir_r4_bundles(
        self,
        content: str,
        person_id: Optional[str] = None,
    ) -> ConvertCombinedFhirR4BundlesResponse:
        """
        This operation aggregates information retrieved from prior Convert API requests into a single entry.

        ### Parameters

        - `fhir_bundles`: A newline-delimited JSON list of FHIR R4 Bundles
        - `patient_id`: The patient ID to use for the FHIR bundle

        ### Returns

        A single FHIR R4 Bundle containing the merged data from the input.

        ### Documentation

        <https://rosetta-api.docs.careevolution.com/convert/combine_bundles.html>
        """
        headers = {"Content-Type": "application/x-ndjson"}
        route = _get_id_dependent_route("/convert/v1/combinefhirr4bundles", person_id)
        return self._post(
            path=route,
            body=content,
            headers=headers,
        )
