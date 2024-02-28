from typing import Optional, TypedDict, overload
from orchestrate._internal.http_handler import create_local_hashing_http_handler
from orchestrate._internal.identity.demographic import (
    BlindedDemographic,
    Demographic,
    demographic_api_method_overload_handler,
)
from orchestrate._internal.identity.advisories import Advisories


class HashDemographicResponse(BlindedDemographic, TypedDict):
    advisories: Advisories


class LocalHashingApi:
    def __init__(self, url: Optional[str] = None) -> None:
        self.__http_handler = create_local_hashing_http_handler(base_url=url)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self.__http_handler.base_url!r})"

    @overload
    def hash_(self, demographic: Demographic) -> HashDemographicResponse:
        """
        Hashes a demographic using the local hashing service.

        ### Parameters

        - `demographic`: The demographic to hash.

        ### Returns

        The hashed demographic.

        - `data`: The B64 encoded hash provided by the local hashing service.
        - `version`: The version number provided by the local hashing service.
        - `advisories`: Contains advisory messages about the operation.

        ### Documentation

        <>
        """
        ...

    @overload
    def hash_(
        self,
        *,
        first_name: Optional[str] = None,
        middle_name: Optional[str] = None,
        last_name: Optional[str] = None,
        maiden_name: Optional[str] = None,
        gender: Optional[str] = None,
        race: Optional[str] = None,
        home_phone_number: Optional[str] = None,
        cell_phone_number: Optional[str] = None,
        email: Optional[str] = None,
        dob: Optional[str] = None,
        street: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        zip_code: Optional[str] = None,
        mrn: Optional[str] = None,
        hcid: Optional[str] = None,
        ssn: Optional[str] = None,
        medicaid_id: Optional[str] = None,
    ) -> HashDemographicResponse:
        """
        Hashes a demographic using the local hashing service.

        ### Parameters

        All parameters are keyword-only.

        - `first_name`
        - `middle_name`
        - `last_name`
        - `maiden_name`
        - `gender`: A HL7 administrative gender category code (i.e., male, female, other, unknown).
        - `race`: A HL7 race category code (e.g., 2054-5 means “Black or African American”).
        - `home_phone_number`
        - `cell_phone_number`
        - `email`
        - `dob`: Date of birth in yyyy/mm/dd or yyyy-mm-dd format.
        - `street`: Street address.
        - `city`
        - `state`: Two-letter state abbreviation.
        - `zip_code`: Postal or Zip code.
        - `mrn`: A medical record number, often used by electronic medical record systems.
        - `hcid`: A Health Card Identifier, such as an enrollee ID on an insurance plan.
        - `ssn`: Either the full 9 or last 4 digits of a Social Security Number.
        - `medicaid_id`: The Medicaid ID number.

        ### Returns

        The hashed demographic.

        - `data`: The B64 encoded hash provided by the local hashing service.
        - `version`: The version number provided by the local hashing service.
        - `advisories`: Contains advisory messages about the operation.

        ### Documentation

        <>
        """

    def hash_(self, *args, **kwargs):
        overload_handler = demographic_api_method_overload_handler(
            self.__http_handler, *args, **kwargs
        )
        return overload_handler("/hash")
