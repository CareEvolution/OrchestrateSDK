from typing import Generic, Literal, Optional, TypeVar, TypedDict, Union


class Coding(TypedDict):
    system: Optional[str]
    code: Optional[str]
    display: Optional[str]


class CodeableConcept(TypedDict):
    coding: list[Coding]
    text: str


class Resource(TypedDict):
    id: str
    resourceType: str


class ValueSet(TypedDict):
    id: str
    resourceType: Literal["ValueSet"]
    compose: dict


class MeasureReport(TypedDict):
    id: str
    resourceType: Literal["MeasureReport"]


class Measure(TypedDict):
    id: str
    resourceType: Literal["Measure"]


class RiskAssessment(TypedDict):
    id: str
    resourceType: Literal["RiskAssessment"]


class Patient(TypedDict):
    id: str
    resourceType: Literal["Patient"]


class CodeSystem(TypedDict):
    id: str
    resourceType: Literal["CodeSystem"]
    concept: list
    count: int


class OperationOutcome(TypedDict):
    id: str
    resourceType: Literal["OperationOutcome"]


class BundleEntry(TypedDict):
    resource: Resource


class Bundle(TypedDict):
    id: str
    resourceType: Literal["Bundle"]
    entry: list[BundleEntry]


class SummarizingBundle(Bundle, TypedDict):
    total: int


class Parameter(TypedDict):
    name: str
    valueString: str


class Parameters(TypedDict):
    id: str
    resourceType: Literal["Parameters"]
    parameter: list[Parameter]
