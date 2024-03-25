from typing import Literal, TypedDict
from orchestrate._internal.http_handler import HttpHandler

IdentifierMetricsRecordType = Literal[
    "City",
    "DOB",
    "Email",
    "FirstName",
    "Gender",
    "HighwayNumber",
    "HighwayPrefix",
    "LastFourSSN",
    "LastName",
    "MaidenName",
    "MiddleName",
    "Ordinal",
    "PO",
    "POBoxNumber",
    "PhoneNumber",
    "SSN",
    "State",
    "StreetFraction",
    "StreetName",
    "StreetNumber",
    "StreetNumberAlpha",
    "StreetType",
    "UnitNumber",
    "UnitNumberAlpha",
    "UnitType",
    "ZipCode",
    "ZipCodeExtension",
]


class IdentifierMetricsRecord(TypedDict):
    identifierType: IdentifierMetricsRecordType
    recordCount: int
    recordRatio: float
    source: str


class GlobalIdentifierMetricsRecord(IdentifierMetricsRecord, TypedDict):
    source: Literal[""]  # type: ignore


class SourceTotal(TypedDict):
    source: str
    totalRecordCount: int


class IdentifierMetricsResponse(TypedDict):
    refreshed: str
    totalRecordCount: int
    totalPersonCount: int
    globalMetricsRecords: list[GlobalIdentifierMetricsRecord]
    summaryMetricsRecords: list[IdentifierMetricsRecord]
    sourceTotals: list[SourceTotal]


class DatasourceOverlapRecord(TypedDict):
    datasourceA: str
    datasourceB: str
    overlapCount: int


class OverlapMetricsResponse(TypedDict):
    datasourceOverlapRecords: list[DatasourceOverlapRecord]


class IdentityMonitoringApi:
    def __init__(self, http_handler: HttpHandler):
        self.__http_handler = http_handler

    def identifier_metrics(self) -> IdentifierMetricsResponse:
        """
        Queries identifier metrics. The identifier metrics help you understand:

        - How many records you have stored.
        - How often different kinds of demographic identifiers are found in your records.
        - What kind and how many demographic identifiers different data sources provide.

        ### Returns

        The identifier metrics

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/metrics/identifier.html>
        """
        return self.__http_handler.get("/monitoring/v1/identifierMetrics")

    def overlap_metrics(self) -> OverlapMetricsResponse:
        """
        Queries overlap metrics. The overlap metrics help you understand how many patients have records in multiple source systems.

        ### Returns

        The overlap metrics

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/metrics/overlap.html>
        """
        return self.__http_handler.get("/monitoring/v1/overlapMetrics")
