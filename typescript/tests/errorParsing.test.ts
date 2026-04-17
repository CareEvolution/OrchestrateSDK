import { describe, it, expect, vi, afterEach } from "vitest";
import { HttpHandler } from "../src/httpHandler";
import { OrchestrateClientError, OperationOutcomeIssue } from "../src/exceptions";

const CDA_TO_FHIR_OPERATION_OUTCOME = {
  resourceType: "OperationOutcome",
  issue: [
    {
      severity: "error",
      code: "invalid",
      diagnostics: "Missing recordTarget in ClinicalDocument",
    },
    {
      severity: "information",
      code: "informational",
      details: {
        coding: [
          {
            system: "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage",
            code: "DocumentId",
          },
        ],
        text: "fb04306a-0834-432d-90c3-251ed7d3401d",
      },
    },
    {
      severity: "information",
      code: "informational",
      details: {
        coding: [
          {
            system: "https://quality.rosetta.careevolution.com/v1/CodeSystems/CDAProcessingMessage",
            code: "DocumentEffectiveTime",
          },
        ],
        text: "2011-05-27T01:44:27-05:00",
      },
    },
  ],
};

function makeFakeResponse(payload: object, status: number) {
  return {
    ok: false,
    status,
    text: async () => JSON.stringify(payload),
  };
}

describe("OrchestrateClientError structured issue parsing", () => {
  const handler = new HttpHandler(
    "https://api.example.com",
    { "Content-Type": "application/json", Accept: "application/json" },
    10_000,
  );

  afterEach(() => {
    vi.unstubAllGlobals();
  });

  async function getErrorFromFakeResponse(payload: object, status: number): Promise<OrchestrateClientError> {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(makeFakeResponse(payload, status)));
    try {
      await handler.post("/convert/v1/cdatofhirr4", "<ClinicalDocument/>");
      throw new Error("Expected OrchestrateClientError to be thrown");
    } catch (e) {
      if (e instanceof OrchestrateClientError) return e;
      throw e;
    }
  }

  it("should capture all issues from a multi-issue OperationOutcome", async () => {
    const error = await getErrorFromFakeResponse(CDA_TO_FHIR_OPERATION_OUTCOME, 400);

    expect(error.issues).toHaveLength(3);
    expect(error.issues[0]).toBeInstanceOf(OperationOutcomeIssue);
  });

  it("should parse an error issue with diagnostics and no details", async () => {
    const error = await getErrorFromFakeResponse(CDA_TO_FHIR_OPERATION_OUTCOME, 400);

    const issue = error.issues[0];
    expect(issue.severity).toBe("error");
    expect(issue.code).toBe("invalid");
    expect(issue.diagnostics).toBe("Missing recordTarget in ClinicalDocument");
    expect(issue.details).toBe("");
  });

  it("should extract details.text for information issues", async () => {
    const error = await getErrorFromFakeResponse(CDA_TO_FHIR_OPERATION_OUTCOME, 400);

    const docIdIssue = error.issues[1];
    expect(docIdIssue.severity).toBe("information");
    expect(docIdIssue.code).toBe("informational");
    expect(docIdIssue.details).toBe("fb04306a-0834-432d-90c3-251ed7d3401d");
    expect(docIdIssue.diagnostics).toBe("");

    const effectiveTimeIssue = error.issues[2];
    expect(effectiveTimeIssue.details).toBe("2011-05-27T01:44:27-05:00");
  });

  it("should preserve statusCode and responseText", async () => {
    const error = await getErrorFromFakeResponse(CDA_TO_FHIR_OPERATION_OUTCOME, 400);

    expect(error.statusCode).toBe(400);
    expect(error.responseText).toBe(JSON.stringify(CDA_TO_FHIR_OPERATION_OUTCOME));
  });

  it("should include all issue texts in the error message", async () => {
    const error = await getErrorFromFakeResponse(CDA_TO_FHIR_OPERATION_OUTCOME, 400);

    expect(error.message).toContain("Missing recordTarget in ClinicalDocument");
    expect(error.message).toContain("fb04306a-0834-432d-90c3-251ed7d3401d");
    expect(error.message).toContain("2011-05-27T01:44:27-05:00");
  });
});
