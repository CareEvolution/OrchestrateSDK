from orchestrate._internal.identity.demographic import (
    demographic_to_dict,
    demographic_from_dict,
    Demographic,
)


def test_demographic_to_dict_should_camel_case():
    demographic = Demographic(
        first_name="John",
        last_name="Doe",
        dob="1980-01-01",
    )

    result = demographic_to_dict(demographic)

    assert result["firstName"] == "John"
    assert result["lastName"] == "Doe"
    assert result["dob"] == "1980-01-01"


def test_demographic_from_dict_should_read_from_camel_case():
    dict_demographic = {"firstName": "John", "lastName": "Doe", "dob": "1980-01-01"}

    result = demographic_from_dict(dict_demographic)

    assert result == Demographic(
        first_name="John",
        last_name="Doe",
        dob="1980-01-01",
    )


def test_demographic_dict_methods_should_interoperate():
    demographic = Demographic(
        first_name="John",
        last_name="Doe",
        dob="1980-01-01",
    )
    json_demographic = demographic_to_dict(demographic)

    result = demographic_from_dict(json_demographic)

    assert result == demographic
