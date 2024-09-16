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
            "hcc_version": hcc_version,
            "period_end_date": period_end_date,
            "ra_segment": ra_segment,
        }
        return self.__http_handler.post(
            path="/insight/v1/riskprofile",
            body=content,
            parameters=parameters,
        )
