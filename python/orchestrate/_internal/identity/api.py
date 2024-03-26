from typing import Any, Callable, Literal, Optional, TypedDict, Union, overload
from urllib.parse import quote_plus
from orchestrate._internal.http_handler import create_identity_http_handler
from orchestrate._internal.identity.advisories import Advisories
from orchestrate._internal.identity.demographic import (
    Demographic,
    demographic_api_method_overload_handler,
)
from orchestrate._internal.identity.local_hashing import BlindedDemographic
from orchestrate._internal.identity.monitoring import IdentityMonitoringApi


class PersonStatus(TypedDict):
    code: Literal["Active", "Retired"]
    supercededBy: list[str]


class Record(TypedDict):
    source: str
    identifier: str


class Person(TypedDict):
    id: str
    records: list[Record]
    version: int
    status: PersonStatus


class MatchedPersonReference(TypedDict):
    matchedPerson: Person
    changedPersons: list[Person]


class AddOrUpdateRecordResponse(MatchedPersonReference, TypedDict):
    advisories: Advisories


AddOrUpdateBlindedRecordResponse = MatchedPersonReference

GetPersonByRecordResponse = Person

GetPersonByIdResponse = Person


class MatchDemographicsResponse(TypedDict):
    matchingPersons: list[Person]
    advisories: list[Advisories]


MatchBlindedDemographicRequest = BlindedDemographic


class MatchBlindedDemographicsResponse(TypedDict):
    matchingPersons: list[Person]


class DeleteRecordResponse(TypedDict):
    changedPersons: list[Person]


class AddMatchGuidanceResponse(TypedDict):
    changedPersons: list[Person]


class RemoveMatchGuidanceResponse(TypedDict):
    changedPersons: list[Person]


def _get_source_identifier_route(source: str, identifier: str) -> str:
    return f"{quote_plus(source)}/{quote_plus(identifier)}"


def _split_source_identifier_route_parameters(
    *args, **kwargs
) -> tuple[str, list[Union[str, dict]], dict[str, Any]]:
    source = args[0] if len(args) > 0 else kwargs["source"]
    identifier = args[1] if len(args) > 1 else kwargs["identifier"]
    remaining_args = list(args[2:]) if len(args) > 2 else []
    remaining_kwargs = {
        key: value
        for key, value in kwargs.items()
        if key not in ["source", "identifier"]
    }
    return (
        _get_source_identifier_route(source=source, identifier=identifier),
        remaining_args,
        remaining_kwargs,
    )


def _get_blinded_request(
    *args,
    **kwargs,
) -> BlindedDemographic:
    if (
        args
        and isinstance(args[0], dict)
        and all(request_key in ["data", "version"] for request_key in args[0])
    ):
        return {
            "data": args[0]["data"],
            "version": args[0]["version"],
        }
    elif isinstance(kwargs.get("blinded_demographic"), dict):
        return {
            "data": kwargs["blinded_demographic"]["data"],
            "version": kwargs["blinded_demographic"]["version"],
        }
    if any(argument not in ["data", "version"] for argument in kwargs.keys()):
        raise TypeError("Unable to determine blinded method from arguments")
    return {
        "data": kwargs["data"],
        "version": kwargs["version"],
    }


class IdentityApi:
    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        metrics_key: Optional[str] = None,
    ) -> None:
        self.__http_handler = create_identity_http_handler(
            api_key=api_key, metrics_key=metrics_key, base_url=url
        )
        self.monitoring = IdentityMonitoringApi(self.__http_handler)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(base_url={self.__http_handler.base_url!r})"

    def __demographic_api_method_overload_handler(
        self, *args, **kwargs
    ) -> Callable[[str], Any]:
        return demographic_api_method_overload_handler(
            self.__http_handler, *args, **kwargs
        )

    @overload
    def add_or_update_record(
        self,
        source: str,
        identifier: str,
        demographic: Demographic,
    ) -> AddOrUpdateRecordResponse:
        """
        Adds a new record or updates a previously created one.

        ### Parameters

        - `source`: The system from which the record demographics were sourced.
        - `identifier`: The unique identifier of the record within the source.
        - `demographic`: The demographic information of the record.

        ### Returns

        The record's assigned person ID, along with any changes resulting from the addition or update.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/add_update_record.html>
        """
        ...

    @overload
    def add_or_update_record(
        self,
        source: str,
        identifier: str,
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
    ) -> AddOrUpdateRecordResponse:
        """
        Adds a new record or updates a previously created one.

        ### Parameters

        - `source`: The system from which the record demographics were sourced.
        - `identifier`: The unique identifier of the record within the source.

        Demographic parameters are keyword-only.

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

        The record's assigned person ID, along with any changes resulting from the addition or update.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/add_update_record.html>
        """
        ...

    def add_or_update_record(
        self,
        *args,
        **kwargs,
    ) -> AddOrUpdateRecordResponse:
        source_identifier, remaining_args, remaining_kwargs = (
            _split_source_identifier_route_parameters(*args, **kwargs)
        )
        handler = self.__demographic_api_method_overload_handler(
            *remaining_args, **remaining_kwargs
        )
        route = f"/mpi/v1/record/{source_identifier}"
        return handler(route)

    @overload
    def add_or_update_blinded_record(
        self,
        source: str,
        identifier: str,
        *,
        data: str,
        version: int,
    ) -> AddOrUpdateBlindedRecordResponse:
        """
        Adds a new record or updates a previously created one in privacy-preserving (blinded) mode.

        ### Parameters

        - `source`: The system from which the record demographics were sourced.
        - `identifier`: The unique identifier of the record within the source.

        Demographic parameters are keyword-only.

        - `data`: The B64 encoded hash provided by the local hashing service.
        - `version`: The version number provided by the local hashing service.

        ### Returns

        Returns the record's assigned person ID, along with any changes resulting from the addition or update.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/add_update_record_blinded.html>
        """
        ...

    @overload
    def add_or_update_blinded_record(
        self,
        source: str,
        identifier: str,
        blinded_demographic: BlindedDemographic,
    ) -> AddOrUpdateBlindedRecordResponse:
        """
        Adds a new record or updates a previously created one in privacy-preserving (blinded) mode.

        ### Parameters

        - `source`: The system from which the record demographics were sourced.
        - `identifier`: The unique identifier of the record within the source.
        - `request`: The request object containing the B64 encoded hash and version number.

        ### Returns

        Returns the record's assigned person ID, along with any changes resulting from the addition or update.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/add_update_record_blinded.html>
        """
        ...

    def add_or_update_blinded_record(
        self,
        *args,
        **kwargs,
    ) -> AddOrUpdateBlindedRecordResponse:
        source_identifier, remaining_args, remaining_kwargs = (
            _split_source_identifier_route_parameters(*args, **kwargs)
        )
        request = _get_blinded_request(*remaining_args, **remaining_kwargs)
        return self.__http_handler.post(
            f"/mpi/v1/blindedRecord/{source_identifier}", body=request
        )

    def get_person_by_record(
        self, source: str, identifier: str
    ) -> GetPersonByRecordResponse:
        """
        Given a source system and identifier, this retrieves the person's metadata (including their Person ID) and the collection of records grouped with that individual.

        ### Parameters

        - `source`: The system from which the record demographics were sourced.
        - `identifier`: The unique identifier of the record within the source.

        ### Returns

        The matched person.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/get_person_by_record.html>
        """
        source_identifier, _, _ = _split_source_identifier_route_parameters(
            source=source, identifier=identifier
        )
        return self.__http_handler.get(f"/mpi/v1/record/{source_identifier}")

    def get_person_by_id(self, id_: str) -> GetPersonByIdResponse:
        """
        Given a Person ID, this retrieves the person's metadata and the collection of records grouped with that individual.

        ### Parameters

        - `id_`: id of the person to fetch

        ### Returns

        The matched person

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/get_person_by_id.html>
        """
        return self.__http_handler.get(f"/mpi/v1/person/{quote_plus(id_)}")

    @overload
    def match_demographics(
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
    ) -> MatchDemographicsResponse:
        """
        Finds all persons and their associated records that match the provided demographics. This operation is read-only, and will not create or update any person records.

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

        Persons and their associated records that match the provided demographics.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/match_demographics.html>
        """
        ...

    @overload
    def match_demographics(self, demographic: Demographic) -> MatchDemographicsResponse:
        """
        Finds all persons and their associated records that match the provided demographics. This operation is read-only, and will not create or update any person records.

        ### Parameters

        - `demographic`: The demographic information of the record.

        ### Returns

        Persons and their associated records that match the provided demographics.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/match_demographics.html>
        """
        ...

    def match_demographics(self, *args, **kwargs) -> MatchDemographicsResponse:
        handler = self.__demographic_api_method_overload_handler(*args, **kwargs)
        return handler("/mpi/v1/match")

    @overload
    def match_blinded_demographics(
        self,
        *,
        data: str,
        version: int,
    ) -> MatchBlindedDemographicsResponse:
        """
        Finds all persons and their associated records that match the provided demographics in privacy-preserving (blinded) mode.

        ### Parameters

        All parameters are keyword-only.

        - `data`: The B64 encoded hash provided by the local hashing service.
        - `version`: The version number provided by the local hashing service.

        ### Returns

        Persons and their associated records that match the provided demographics.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/match_demographics_blinded.html>
        """
        ...

    @overload
    def match_blinded_demographics(
        self, blinded_demographic: MatchBlindedDemographicRequest
    ) -> MatchBlindedDemographicsResponse:
        """
        Finds all persons and their associated records that match the provided demographics. This operation is read-only, and will not create or update any person records.

        ### Parameters

        - `request`: The demographic information of the record.

        ### Returns

        Persons and their associated records that match the provided demographics.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/match_demographics_blinded.html>
        """
        ...

    def match_blinded_demographics(
        self,
        *args,
        **kwargs,
    ) -> MatchBlindedDemographicsResponse:
        request = _get_blinded_request(*args, **kwargs)
        return self.__http_handler.post(f"/mpi/v1/matchBlinded", body=request)

    def delete_record(self, source: str, identifier: str) -> DeleteRecordResponse:
        """
        Deletes a record using a source system and identifier.

        ### Parameters

        - `source`: The system from which the record demographics were sourced.
        - `identifier`: The unique identifier of the record within the source.

        ### Returns

        List of persons changed by the operation.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/delete_record.html>
        """
        route = _get_source_identifier_route(source=source, identifier=identifier)
        return self.__http_handler.post(f"/mpi/v1/deleteRecord/{route}", body={})

    def add_match_guidance(
        self,
        record_one: Union[Record, dict[str, str]],
        record_two: Union[Record, dict[str, str]],
        action: Literal["Match", "NoMatch"],
        comment: str,
    ) -> AddMatchGuidanceResponse:
        """
        Overrides automatic matching with manual guidance for a particular set of records.

        ### Parameters

        - `record_one`: The first record
        - `record_two`: The second record
        - `action`: Use Match if the two records represent the same individual, and NoMatch if the two records represent different individuals.
        - `comment`: A comment for documentation/audit purposes.

        ### Returns

        List of persons changed by the operation.

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/add_guidance.html>
        """
        body = {
            "recordOne": record_one,
            "recordTwo": record_two,
            "action": action,
            "comment": comment,
        }
        return self.__http_handler.post("/mpi/v1/addGuidance", body=body)

    def remove_match_guidance(
        self,
        record_one: Union[Record, dict[str, str]],
        record_two: Union[Record, dict[str, str]],
        comment: str,
    ) -> RemoveMatchGuidanceResponse:
        """
        Removes a previously-created manual match guidance.

        ### Parameters

        - `record_one`: The first record
        - `record_two`: The second record
        - `comment`: A comment for documentation/audit purposes.

        ### Returns

        List of persons changed by the operation

        ### Documentation

        <https://orchestrate.docs.careevolution.com/identity/operations/remove_guidance.html>
        """
        body = {
            "recordOne": record_one,
            "recordTwo": record_two,
            "comment": comment,
        }
        return self.__http_handler.post("/mpi/v1/removeGuidance", body=body)
