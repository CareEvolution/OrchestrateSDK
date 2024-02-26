from dataclasses import asdict, dataclass, field
import json
import re
from typing import Optional


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


def demographic_to_json(demographic: Demographic) -> str:
    default_dictionary = asdict(demographic)
    dictionary = {
        _CAMELCASE.sub(lambda match: f"_{match.group(1).lower()}", key): value
        for key, value in default_dictionary.items()
        if value is not None
    }

    return json.dumps(dictionary)


def demographic_from_json(json_string: str) -> Demographic:
    dictionary = json.loads(json_string)
    dictionary = {
        _SNAKECASE.sub(lambda match: match.group(1).upper(), key): value
        for key, value in dictionary.items()
    }

    return Demographic(**dictionary)
