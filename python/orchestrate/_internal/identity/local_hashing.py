from typing import Any, Optional, TypedDict, overload
from orchestrate._internal.http_handler import create_http_handler
from orchestrate._internal.identity.demographic import Demographic, demographic_to_json

InvalidDemographicField = dict[str, Any]


class HashDemographicResponseAdvisories(TypedDict):
    invalidDemographicFields: list[InvalidDemographicField]


class HashDemographicResponse(TypedDict):
    data: str
    version: int
    advisories: HashDemographicResponseAdvisories


class LocalHashingApi:
    def __init__(self, api_key: str) -> None:
        self.__http_handler = create_http_handler(api_key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self.__http_handler.base_url!r})"

    @overload
    def hash_(self, demographic: Demographic) -> HashDemographicResponse:
        """
        Hashes a demographic using the local hashing service.

        ### Parameters

        - `demographic`: (Demographic): The demographic to hash.

        ### Returns

        The hashed demographic.
        """
        json_demographic = demographic_to_json(demographic)
        return self.__http_handler.post(
            "/hash",
            json_demographic,
        )

    @overload
    def hash_(self,
              first_name: Optional[str],
    middle_name: Optional[str],
    last_name: Optional[str],
    maiden_name: Optional[str],
    gender: Optional[str],
    race: Optional[str],
    home_phone_number: Optional[str],
    cell_phone_number: Optional[str],
    email: Optional[str],
    dob: Optional[str],
    street: Optional[str],
    city: Optional[str],
    state: Optional[str],
    zip_code: Optional[str],
    mrn: Optional[str],
    hcid: Optional[str],
    ssn: Optional[str],
    medicaid_id: Optional[str],) -> HashDemographicResponse:
