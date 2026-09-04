import { describe, expect, it } from "vitest";
import { TerminologyApi } from "../src/terminology";
import type { IHttpHandler } from "../src/httpHandler";

class FakeHttpHandler implements IHttpHandler {
  lastPath?: string;
  lastBody?: unknown;

  async post<TIn, TOut>(path: string, body: TIn): Promise<TOut> {
    this.lastPath = path;
    this.lastBody = body;
    return { resourceType: "Parameters", parameter: [] } as TOut;
  }

  async get<TOut>(): Promise<TOut> {
    throw new Error("not implemented");
  }
}

const coding = (body: unknown) =>
  (body as { parameter: { name: string; valueCoding?: unknown }[] }).parameter.find((p) => p.name === "coding")
    ?.valueCoding;

const names = (body: unknown) => (body as { parameter: { name: string }[] }).parameter.map((p) => p.name);

describe("translateFhirR4ConceptMap", () => {
  it("posts to the translate route", async () => {
    const handler = new FakeHttpHandler();
    const terminology = new TerminologyApi(handler);

    await terminology.translateFhirR4ConceptMap({ code: "119981000146107" });

    expect(handler.lastPath).toBe("/terminology/v1/fhir/r4/conceptmap/$translate");
  });

  it("builds a coding parameter from code alone", async () => {
    const handler = new FakeHttpHandler();
    const terminology = new TerminologyApi(handler);

    await terminology.translateFhirR4ConceptMap({ code: "119981000146107" });

    expect((handler.lastBody as { resourceType: string }).resourceType).toBe("Parameters");
    expect(names(handler.lastBody)).toEqual(["coding"]);
    expect(coding(handler.lastBody)).toEqual({ code: "119981000146107" });
  });

  it("adds a domain parameter when a domain is given", async () => {
    const handler = new FakeHttpHandler();
    const terminology = new TerminologyApi(handler);

    await terminology.translateFhirR4ConceptMap({
      code: "119981000146107",
      domain: "DiagnosisCode",
    });

    expect(names(handler.lastBody)).toEqual(["domain", "coding"]);
    const body = handler.lastBody as { parameter: { name: string; valueString?: string }[] };
    expect(body.parameter.find((p) => p.name === "domain")?.valueString).toBe("DiagnosisCode");
  });

  it("carries system and display into the coding", async () => {
    const handler = new FakeHttpHandler();
    const terminology = new TerminologyApi(handler);

    await terminology.translateFhirR4ConceptMap({
      code: "119981000146107",
      system: "http://snomed.info/sct",
      display: "Essential hypertension",
    });

    expect(coding(handler.lastBody)).toEqual({
      system: "http://snomed.info/sct",
      code: "119981000146107",
      display: "Essential hypertension",
    });
  });

  it("allows display without code", async () => {
    const handler = new FakeHttpHandler();
    const terminology = new TerminologyApi(handler);

    await terminology.translateFhirR4ConceptMap({ display: "Essential hypertension" });

    expect(coding(handler.lastBody)).toEqual({ display: "Essential hypertension" });
  });

  it("drops empty fields", async () => {
    const handler = new FakeHttpHandler();
    const terminology = new TerminologyApi(handler);

    await terminology.translateFhirR4ConceptMap({ code: "119981000146107", system: "" });

    expect(coding(handler.lastBody)).toEqual({ code: "119981000146107" });
    expect(names(handler.lastBody)).toEqual(["coding"]);
  });

  it("treats whitespace-only fields as absent", async () => {
    const handler = new FakeHttpHandler();
    const terminology = new TerminologyApi(handler);

    await terminology.translateFhirR4ConceptMap({ code: "119981000146107", system: "   " });

    expect(coding(handler.lastBody)).toEqual({ code: "119981000146107" });
  });

  it("omits the domain parameter when domain is whitespace-only", async () => {
    const handler = new FakeHttpHandler();
    const terminology = new TerminologyApi(handler);

    await terminology.translateFhirR4ConceptMap({
      code: "119981000146107",
      // eslint-disable-next-line @typescript-eslint/no-explicit-any -- exercising a caller that bypasses the type system
      domain: "   " as any,
    });

    expect(names(handler.lastBody)).toEqual(["coding"]);
  });

  it("omits the coding parameter when all coding fields are absent", async () => {
    const handler = new FakeHttpHandler();
    const terminology = new TerminologyApi(handler);

    await terminology.translateFhirR4ConceptMap({ system: "  " });

    expect((handler.lastBody as { parameter: unknown[] }).parameter).toEqual([]);
  });
});
