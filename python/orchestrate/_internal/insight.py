from typing import Literal, Optional

from orchestrate._internal.fhir import Bundle
from orchestrate._internal.http_handler import HttpHandler
from typing import Literal, TypedDict, Union
from orchestrate._internal.fhir import (
    Measure,
    MeasureReport,
    OperationOutcome,
    Patient,
    RiskAssessment,
    ValueSet,
)


class InsightBundleEntry(TypedDict):
    resource: Union[
        Patient,
        MeasureReport,
        Measure,
        ValueSet,
        RiskAssessment,
        OperationOutcome,
    ]


class InsightBundle(TypedDict):
    id: str
    resourceType: Literal["Bundle"]
    entry: list[InsightBundleEntry]


InsightRiskProfileResponse = InsightBundle

InsightFhirR4ToManifestResponse = bytes


class InsightApi:
    def __init__(self, http_handler: HttpHandler) -> None:
        self.__http_handler = http_handler

    def risk_profile(
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

        <https://orchestrate.docs.careevolution.com/insight/risk_profile.html>
        """
        parameters = {
            "hccVersion": hcc_version,
            "periodEndDate": period_end_date,
            "raSegment": ra_segment,
        }
        return self.__http_handler.post(
            path="/insight/v1/riskprofile",
            body=content,
            parameters=parameters,
        )

    def fhir_r4_to_manifest(self, content: Bundle) -> InsightFhirR4ToManifestResponse:
        """
        Generates a tabular report of clinical concepts from a FHIR R4
        bundle. With this tabular data, you can easily scan results, run
        queries, and understand the value of your clinical data.

        ### Parameters

        - `content`: A FHIR R4 bundle

        ### Returns

        A ZIP file containing a number of Comma-Separated Value (CSV)
        files corresponding to clinical concepts (conditions,
        encounters, etc.).

        ### Documentation

        <https://orchestrate.docs.careevolution.com/insight/fhir_manifest.html>
        """
        headers = {
            "Accept": "application/zip",
        }
        return self.__http_handler.post(
            path="/insight/v1/fhirr4tomanifest",
            body=content,
            headers=headers,
        )
