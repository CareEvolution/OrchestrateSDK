import { describe, expect, test } from "vitest";
import { HttpHandler } from "../src/httpHandler";
import { parse } from "dotenv";
import { existsSync, readFileSync } from "fs";

class OutcomeTestCase {
  contentType: string;
  accept: string;
  route: string;
  body: any; // eslint-disable-line @typescript-eslint/no-explicit-any
  expectedMessage: string;
  id: string;
}

describe.concurrent("httpHandler outcomes", () => {
  const testCases: OutcomeTestCase[] = [
    {
      contentType: "application/json",
      accept: "application/json",
      route: "/convert/v1/fhirstu3tofhirr4",
      body: { "resourceType": "Patient" },
      expectedMessage: "error: invalid - Expected a Bundle but found a Patient",
      id: "json",
    },
    {
      contentType: "application/json",
      accept: "application/xml",
      route: "/convert/v1/fhirstu3tofhirr4",
      body: { "resourceType": "Patient" },
      expectedMessage: "Expected a Bundle but found a Patient",
      id: "xml",
    },
    {
      contentType: "application/xml",
      accept: "text/html",
      route: "/convert/v1/cdatohtml",
      body: "<ClinicalDocument></ClinicalDocument>",
      expectedMessage: "CDA did not render",
      id: "html",
    },
    {
      contentType: "application/xml",
      accept: "application/pdf",
      route: "/convert/v1/cdatopdf",
      body: "<ClinicalDocument></ClinicalDocument>",
      expectedMessage: "CDA did not render",
      id: "pdf",
    },
    {
      contentType: "application/json",
      accept: "application/zip",
      route: "/convert/v1/fhirr4toomop",
      body: { "resourceType": "Patient" },
      expectedMessage: "Expected a Bundle but found a Patient",
      id: "zip",
    },
  ];
  const cases = testCases.map((input) => ({ input }));

  const environment = parse(existsSync(".env") ? readFileSync(".env") : readFileSync("../.env"));
  const handler = new HttpHandler(
    "https://api.careevolutionapi.com",
    {
      "Content-Type": "application/json",
      Accept: "application/json",
      "x-api-key": environment.ORCHESTRATE_API_KEY,
    },
  );

  test.each(cases)("should classify single $input.id", async ({ input }: { input: OutcomeTestCase; }) => {
    const { contentType, accept, route, body, expectedMessage } = input;

    expect(async () => {
      await handler.post(route, body, { "Content-Type": contentType, Accept: accept });
    }).rejects.toThrowError(expectedMessage);
  });
});
