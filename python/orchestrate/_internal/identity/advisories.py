from typing import Any, TypedDict


InvalidDemographicField = dict[str, Any]


class Advisories(TypedDict):
    invalidDemographicFields: list[InvalidDemographicField]
