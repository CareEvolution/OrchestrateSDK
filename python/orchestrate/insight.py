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
