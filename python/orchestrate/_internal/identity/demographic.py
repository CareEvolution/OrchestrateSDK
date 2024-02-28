from dataclasses import asdict, dataclass, field
import re
from typing import Any, Callable, Mapping, Optional, TypedDict

from orchestrate._internal.http_handler import HttpHandler


class BlindedDemographic(TypedDict):
    data: str
    version: int


@dataclass
class Demographic:
    first_name: Optional[str] = field(default=None)
    middle_name: Optional[str] = field(default=None)
    last_name: Optional[str] = field(default=None)
    maiden_name: Optional[str] = field(default=None)
    gender: Optional[str] = field(default=None)
    race: Optional[str] = field(default=None)
    home_phone_number: Optional[str] = field(default=None)
    cell_phone_number: Optional[str] = field(default=None)
    email: Optional[str] = field(default=None)
    dob: Optional[str] = field(default=None)
    street: Optional[str] = field(default=None)
    city: Optional[str] = field(default=None)
    state: Optional[str] = field(default=None)
    zip_code: Optional[str] = field(default=None)
    mrn: Optional[str] = field(default=None)
    hcid: Optional[str] = field(default=None)
    ssn: Optional[str] = field(default=None)
    medicaid_id: Optional[str] = field(default=None)


_CAMELCASE = re.compile(r"([A-Z])")
_SNAKECASE = re.compile(r"_([a-z])")


def demographic_to_dict(demographic: Demographic) -> dict[str, str]:
    default_dictionary = asdict(demographic)
    dictionary = {
        _SNAKECASE.sub(lambda match: match.group(1).upper(), key): value
        for key, value in default_dictionary.items()
        if value is not None
    }

    return dictionary


def demographic_from_dict(demographic_dict: Mapping[str, Optional[str]]) -> Demographic:
    dictionary = {
        _CAMELCASE.sub(lambda match: f"_{match.group(1).lower()}", key): value
        for key, value in demographic_dict.items()
    }

    return Demographic(**dictionary)


def demographic_api_method_overload_handler(
    http_handler: HttpHandler, *args, **kwargs
) -> Callable[[str], Any]:
    if args and isinstance(args[0], Demographic):
        demographic = args[0]
    elif isinstance(kwargs.get("demographic"), Demographic):
        demographic = kwargs["demographic"]
    else:
        demographic = Demographic(
            first_name=kwargs.get("first_name"),
            middle_name=kwargs.get("middle_name"),
            last_name=kwargs.get("last_name"),
            maiden_name=kwargs.get("maiden_name"),
            gender=kwargs.get("gender"),
            race=kwargs.get("race"),
            home_phone_number=kwargs.get("home_phone_number"),
            cell_phone_number=kwargs.get("cell_phone_number"),
            email=kwargs.get("email"),
            dob=kwargs.get("dob"),
            street=kwargs.get("street"),
            city=kwargs.get("city"),
            state=kwargs.get("state"),
            zip_code=kwargs.get("zip_code"),
            mrn=kwargs.get("mrn"),
            hcid=kwargs.get("hcid"),
            ssn=kwargs.get("ssn"),
            medicaid_id=kwargs.get("medicaid_id"),
        )
    demographic_dict = demographic_to_dict(demographic)
    return lambda url: http_handler.post(url, body=demographic_dict)
