import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import {
  IdentityApi,
  type Demographic,
  type ValidateMatchNoMatchReason,
  type ValidateMatchResponse,
} from "../src/identity.js";

function responseCases(): { name: string; response: ValidateMatchResponse }[] {
  const comparison: ValidateMatchNoMatchReason = {
    exactFields: ["LastName"],
    highSimilarityFields: ["FirstName"],
    lowSimilarityFields: ["StreetName"],
    differentFields: ["DOB"],
    recordAMissingFields: ["Email"],
    recordBMissingFields: ["PhoneNumber"],
  };
  return [
    {
      name: "all comparison categories",
      response: { result: "NO_MATCH", noMatchReason: comparison },
    },
    { name: "omitted comparison", response: { result: "NO_MATCH" } },
    {
      name: "null comparison",
      response: { result: "NO_MATCH", noMatchReason: null },
    },
    {
      name: "successful match",
      response: { result: "MATCH", matchReason: "TestRule" },
    },
    {
      name: "empty comparison",
      response: { result: "NO_MATCH", noMatchReason: {} },
    },
    {
      name: "null comparison fields",
      response: {
        result: "NO_MATCH",
        noMatchReason: { exactFields: null, recordAMissingFields: null },
      },
    },
    {
      name: "partial comparison",
      response: {
        result: "NO_MATCH",
        noMatchReason: { differentFields: ["DOB"] },
      },
    },
  ];
}

describe("IdentityApi.validateMatch", () => {
  beforeEach(() => {
    vi.stubEnv("ORCHESTRATE_IDENTITY_METRICS_KEY", "");
    vi.stubEnv("ORCHESTRATE_ADDITIONAL_HEADERS", "{}");
  });

  afterEach(() => {
    vi.unstubAllGlobals();
    vi.unstubAllEnvs();
  });

  it.each(responseCases())("sends demographics and returns $name", async ({ response: expected }) => {
    const fetchMock = vi.fn().mockResolvedValue(
      new Response(JSON.stringify(expected), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      }),
    );
    vi.stubGlobal("fetch", fetchMock);
    const api = new IdentityApi({
      url: "https://identity.example.test",
      apiKey: "test-api-key",
    });

    const demographic1: Demographic = { firstName: "SyntheticAlpha", homePhoneNumber: "212-555-0175" };
    const demographic2: Demographic = { firstName: "SyntheticBeta", email: "synthetic@example.test" };
    const response = await api.validateMatch(demographic1, demographic2);

    expect(response).toEqual(expected);
    expect(fetchMock).toHaveBeenCalledExactlyOnceWith(
      "https://identity.example.test/v1/validateMatch",
      expect.objectContaining({
        method: "POST",
        body: JSON.stringify([
          { firstName: "SyntheticAlpha", homePhoneNumber: "212-555-0175" },
          { firstName: "SyntheticBeta", email: "synthetic@example.test" },
        ]),
      }),
    );
  });
});
