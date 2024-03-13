from requests import HTTPError


class OrchestrateError(Exception):
    """Base class for all Orchestrate exceptions."""

    pass


class OrchestrateHttpError(OrchestrateError, HTTPError):
    """Raised when an HTTP request to the Orchestrate API fails."""

    pass


class OrchestrateClientError(OrchestrateHttpError):
    """Raised when the Orchestrate API returns a 400 status code."""

    def __init__(self, response_text: str, issues: list[str]) -> None:
        if issues:
            string_outcomes = "\n  * ".join(issues)
            super().__init__(f"Issues: \n  * {string_outcomes}")
            return
        super().__init__(f"Client error: {response_text}")
