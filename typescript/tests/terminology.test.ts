import { describe, expect, it, vi } from "vitest";
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

type Paging = { pageNumber?: number; pageSize?: number };
const pagedRoutes = [
  {
    name: "code system",
    path: "/codesystem/LOINC",
    field: "concept",
    filters: { "concept:contains": "blood pressure" },
    call: (api: TerminologyApi, paging: Paging) =>
      api.getFhirR4CodeSystem({ codeSystem: "LOINC", conceptContains: "blood pressure", ...paging }),
  },
  {
    name: "code system summaries",
    path: "/codesystem",
    field: "entry",
    filters: { _summary: "true" },
    call: (api: TerminologyApi, paging: Paging) => api.summarizeFhirR4CodeSystems(paging),
  },
  {
    name: "concept maps",
    path: "/conceptmap",
    field: "entry",
    filters: {},
    call: (api: TerminologyApi, paging: Paging) => api.getFhirR4ConceptMaps(paging),
  },
  {
    name: "value sets",
    path: "/valueset",
    field: "entry",
    filters: { name: "test name", "extension.scope": "http://loinc.org" },
    call: (api: TerminologyApi, paging: Paging) =>
      api.getFhirR4ValueSetsByScope({ name: "test name", scope: "http://loinc.org", ...paging }),
  },
  {
    name: "scope summaries",
    path: "/valueset",
    field: "entry",
    filters: { _summary: "true", "extension.scope": "http://loinc.org" },
    call: (api: TerminologyApi, paging: Paging) =>
      api.summarizeFhirR4ValueSetScope({ scope: "http://loinc.org", ...paging }),
  },
];

describe.each(pagedRoutes)("$name paging", ({ call, path, field, filters }) => {
  it.each([{ pageNumber: 0 }, { pageSize: 2 }])("rejects incomplete paging %j before HTTP", async (paging) => {
    const get = vi.fn();
    await expect(call(new TerminologyApi({ get, post: vi.fn() }), paging)).rejects.toThrow(
      "pageNumber and pageSize must be provided together",
    );
    expect(get).not.toHaveBeenCalled();
  });

  it.each([0, 3])("returns just the requested page %i", async (pageNumber) => {
    const response = { resourceType: field === "concept" ? "CodeSystem" : "Bundle", [field]: [{ id: "one" }] };
    const get = vi.fn().mockResolvedValue(response);
    const api = new TerminologyApi({ get, post: vi.fn() });

    expect(await call(api, { pageNumber, pageSize: 2 })).toBe(response);
    expect(get).toHaveBeenCalledTimes(1);
    const url = new URL(get.mock.calls[0][0], "https://example.test");
    expect(url.pathname).toBe(`/terminology/v1/fhir/r4${path}`);
    expect(Object.fromEntries(url.searchParams)).toEqual({ ...filters, "page.num": String(pageNumber), _count: "2" });
  });

  it.each([false, true])("aggregates short pages with a known total: %s", async (knownTotal) => {
    const first = {
      resourceType: field === "concept" ? "CodeSystem" : "Bundle",
      id: "resource-id",
      ...(field === "entry"
        ? {
            link: [
              { relation: "self", url: "https://example.test/page/0" },
              { relation: "next", url: "https://example.test/page/1" },
              { relation: "alternate", url: "https://example.test/catalog" },
            ],
          }
        : {}),
      ...(knownTotal ? (field === "concept" ? { count: 2 } : { total: 2 }) : {}),
      [field]: [{ id: "one" }],
    };
    const get = vi
      .fn()
      .mockResolvedValueOnce(first)
      .mockResolvedValueOnce({ [field]: [{ id: "two" }] })
      .mockResolvedValueOnce({});
    const api = new TerminologyApi({ get, post: vi.fn() });

    const expected = {
      ...first,
      [field]: [{ id: "one" }, { id: "two" }],
      ...(field === "entry" ? { link: [{ relation: "alternate", url: "https://example.test/catalog" }] } : {}),
    };
    const result = await call(api, {});

    expect(result).toEqual(expected);
    expect(get).toHaveBeenCalledTimes(knownTotal ? 2 : 3);
    get.mock.calls.forEach(([route], index) => {
      const url = new URL(route, "https://example.test");
      expect(url.pathname).toBe(`/terminology/v1/fhir/r4${path}`);
      expect(Object.fromEntries(url.searchParams)).toEqual({ ...filters, "page.num": String(index), _count: "10000" });
    });
  });

  it("stops on an empty first page", async () => {
    const response = { resourceType: field === "concept" ? "CodeSystem" : "Bundle", [field]: [] };
    const get = vi.fn().mockResolvedValue(response);
    expect(await call(new TerminologyApi({ get, post: vi.fn() }), {})).toBe(response);
    expect(get).toHaveBeenCalledTimes(1);
  });

  it("propagates later failures instead of returning partial results", async () => {
    const error = new Error("page failed");
    const get = vi
      .fn()
      .mockResolvedValueOnce({ [field]: [{ id: "one" }] })
      .mockRejectedValueOnce(error);
    await expect(call(new TerminologyApi({ get, post: vi.fn() }), {})).rejects.toBe(error);
    expect(get).toHaveBeenCalledTimes(2);
  });
});
