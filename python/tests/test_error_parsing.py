import json
from unittest.mock import Mock

import pytest
from orchestrate._internal.exceptions import OrchestrateClientError
from orchestrate._internal.http_handler import _exception_from_response

pytestmark = pytest.mark.default

_CDA_TO_FHIR_OPERATION_OUTCOME = {
    "resourceType": "OperationOutcome",
    "issue": [
        {
            "severity": "error",
            "code": "invalid",
            "diagnostics": "Missing recordTarget in ClinicalDocument",
        },
        {
            "severity": "information",
            "code": "informational",
            "details": {
                "coding": [
                    {
                        "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage",
                        "code": "DocumentId",
                    }
                ],
                "text": "fb04306a-0834-432d-90c3-251ed7d3401d",
            },
        },
        {
            "severity": "information",
            "code": "informational",
            "details": {
                "coding": [
                    {
                        "system": "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage",
                        "code": "DocumentEffectiveTime",
                    }
                ],
                "text": "2011-05-27T01:44:27-05:00",
            },
        },
    ],
}


def _make_mock_response(payload: dict, status_code: int) -> Mock:
    response = Mock()
    response.status_code = status_code
    response.text = json.dumps(payload)
    response.json.return_value = payload
    return response


def test_multiple_issues_should_all_be_captured():
    response = _make_mock_response(_CDA_TO_FHIR_OPERATION_OUTCOME, 400)

    exc = _exception_from_response(response)

    assert isinstance(exc, OrchestrateClientError)
    assert len(exc.issues) == 3


def test_error_issue_with_diagnostics_only():
    response = _make_mock_response(_CDA_TO_FHIR_OPERATION_OUTCOME, 400)

    exc = _exception_from_response(response)

    assert isinstance(exc, OrchestrateClientError)
    issue = exc.issues[0]
    assert issue.severity == "error"
    assert issue.code == "invalid"
    assert issue.diagnostics == "Missing recordTarget in ClinicalDocument"
    assert issue.details == ""


def test_information_issue_with_details_text():
    response = _make_mock_response(_CDA_TO_FHIR_OPERATION_OUTCOME, 400)

    exc = _exception_from_response(response)

    assert isinstance(exc, OrchestrateClientError)
    doc_id_issue = exc.issues[1]
    assert doc_id_issue.severity == "information"
    assert doc_id_issue.code == "informational"
    assert doc_id_issue.details == "fb04306a-0834-432d-90c3-251ed7d3401d"
    assert doc_id_issue.diagnostics == ""

    effective_time_issue = exc.issues[2]
    assert effective_time_issue.details == "2011-05-27T01:44:27-05:00"


def test_status_code_and_response_text_are_preserved():
    response = _make_mock_response(_CDA_TO_FHIR_OPERATION_OUTCOME, 400)

    exc = _exception_from_response(response)

    assert isinstance(exc, OrchestrateClientError)
    assert exc.status_code == 400
    assert exc.response_text == response.text


def test_message_string_includes_all_issues():
    response = _make_mock_response(_CDA_TO_FHIR_OPERATION_OUTCOME, 400)

    exc = _exception_from_response(response)

    message = str(exc)
    assert "Missing recordTarget in ClinicalDocument" in message
    assert "fb04306a-0834-432d-90c3-251ed7d3401d" in message
    assert "2011-05-27T01:44:27-05:00" in message
