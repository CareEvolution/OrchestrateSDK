import { describe, expect, it } from "vitest";
import { buildTranslateFhirR4ConceptMapParameters } from "../src/terminology";

const coding = (parameters: { parameter?: { name?: string; valueCoding?: unknown }[] }) =>
  parameters.parameter?.find((p) => p.name === "coding")?.valueCoding;

const names = (parameters: { parameter?: { name?: string }[] }) => parameters.parameter?.map((p) => p.name);

describe("buildTranslateFhirR4ConceptMapParameters", () => {
  it("builds a coding parameter from code alone", () => {
    const result = buildTranslateFhirR4ConceptMapParameters({ code: "119981000146107" });

    expect(result.resourceType).toBe("Parameters");
    expect(names(result)).toEqual(["coding"]);
    expect(coding(result)).toEqual({ code: "119981000146107" });
  });

  it("adds a domain parameter when a domain is given", () => {
    const result = buildTranslateFhirR4ConceptMapParameters({
      code: "119981000146107",
      domain: "DiagnosisCode",
    });

    expect(names(result)).toEqual(["domain", "coding"]);
    expect(result.parameter?.find((p) => p.name === "domain")?.valueString).toBe("DiagnosisCode");
  });

  it("carries system and display into the coding", () => {
    const result = buildTranslateFhirR4ConceptMapParameters({
      code: "119981000146107",
      system: "http://snomed.info/sct",
      display: "Essential hypertension",
    });

    expect(coding(result)).toEqual({
      system: "http://snomed.info/sct",
      code: "119981000146107",
      display: "Essential hypertension",
    });
  });

  it("allows display without code", () => {
    const result = buildTranslateFhirR4ConceptMapParameters({ display: "Essential hypertension" });

    expect(coding(result)).toEqual({ display: "Essential hypertension" });
  });

  it("drops empty fields", () => {
    const result = buildTranslateFhirR4ConceptMapParameters({ code: "119981000146107", system: "" });

    expect(coding(result)).toEqual({ code: "119981000146107" });
    expect(names(result)).toEqual(["coding"]);
  });
});
