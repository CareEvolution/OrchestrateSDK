from dataclasses import dataclass

from requests import HTTPError


class OrchestrateError(Exception):
    """Base class for all Orchestrate exceptions."""

    pass


class OrchestrateHttpError(OrchestrateError, HTTPError):
    """Raised when an HTTP request to the Orchestrate API fails."""

    pass


@dataclass
class OperationOutcomeIssue:
    """A single issue from a FHIR OperationOutcome."""

    severity: str
    code: str
    diagnostics: str
    details: str

    def __str__(self) -> str:
        s = f"{self.severity}: {self.code}"
        message = "; ".join(m for m in [self.details, self.diagnostics] if m)
        if message:
            s += f" - {message}"
        return s


class OrchestrateClientError(OrchestrateHttpError):
    """Raised when the Orchestrate API returns a 4xx or 5xx status code."""

    def __init__(
        self,
        response_text: str,
        issues: list[OperationOutcomeIssue],
        status_code: int = 0,
    ) -> None:
        self.response_text = response_text
        self.issues = issues
        self.status_code = status_code
        if issues:
            string_outcomes = "\n  * ".join(str(i) for i in issues)
            super().__init__(f"Issues: \n  * {string_outcomes}")
        else:
            super().__init__(f"Client error: {response_text}")
