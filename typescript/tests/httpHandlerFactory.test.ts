import { describe, it, expect, vi, beforeAll, afterAll } from "vitest";
import { HttpHandler } from "../src/httpHandler";
import { createHttpHandler } from "../src/httpHandlerFactory";

vi.mock("../src/httpHandler");

describe("createHttpHandler full environment", () => {
  beforeAll(() => {
    vi.stubEnv("ORCHESTRATE_BASE_URL", "https://env.example.com");
    vi.stubEnv("ORCHESTRATE_API_KEY", "env-api-key");
    vi.stubEnv("ORCHESTRATE_ADDITIONAL_HEADERS", JSON.stringify({ "x-custom-header": "custom-value" }));
  });

  it("should prefer the environment variables", () => {
    createHttpHandler(undefined, undefined);

    expect(HttpHandler).toHaveBeenCalledWith(
      "https://env.example.com",
      {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-api-key": "env-api-key",
        "x-custom-header": "custom-value",
      },
      120_000,
    );
  });

  it("should prefer the api key parameter over the environment variable", () => {
    createHttpHandler("my-api-key", undefined, 30_000);

    expect(HttpHandler).toHaveBeenCalledWith(
      "https://env.example.com",
      {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-api-key": "my-api-key",
        "x-custom-header": "custom-value",
      },
      30_000,
    );
  });

  afterAll(() => {
    vi.unstubAllEnvs();
  });
});

describe("createHttpHandler apiKey environment", () => {
  beforeAll(() => {
    vi.stubEnv("ORCHESTRATE_API_KEY", "env-api-key");
  });

  it("should create an HttpHandler with the provided apiKey", () => {
    createHttpHandler(undefined, undefined);

    expect(HttpHandler).toHaveBeenCalledWith(
      "https://api.careevolutionapi.com",
      {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-api-key": "env-api-key",
      },
      120_000,
    );
  });

  it("should prefer the api key parameter over the environment variable", () => {
    createHttpHandler("my-api-key", undefined);

    expect(HttpHandler).toHaveBeenCalledWith(
      "https://api.careevolutionapi.com",
      {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-api-key": "my-api-key",
      },
      120_000,
    );
  });

  afterAll(() => {
    vi.unstubAllEnvs();
  });
});

describe("createHttpHandler timeoutMs environment", () => {
  beforeAll(() => {
    vi.stubEnv("ORCHESTRATE_API_KEY", "env-api-key");
    vi.stubEnv("ORCHESTRATE_TIMEOUT_MS", "1000");
  });

  it("should create an HttpHandler with the provided timeout", () => {
    createHttpHandler(undefined, undefined);

    expect(HttpHandler).toHaveBeenCalledWith(
      "https://api.careevolutionapi.com",
      {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-api-key": "env-api-key",
      },
      1_000,
    );
  });

  it("should prefer the api key parameter over the environment variable", () => {
    createHttpHandler(undefined, undefined, 2_000);

    expect(HttpHandler).toHaveBeenCalledWith(
      "https://api.careevolutionapi.com",
      {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-api-key": "env-api-key",
      },
      2_000,
    );
  });

  afterAll(() => {
    vi.unstubAllEnvs();
  });
});

describe("createHttpHandler no environment", () => {
  it("should create an HttpHandler defaulted to api.careevolutionapi.com", () => {
    createHttpHandler(undefined, undefined);

    expect(HttpHandler).toHaveBeenCalledWith(
      "https://api.careevolutionapi.com",
      {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      120_000,
    );
  });

  it("should create an HttpHandler with the provided apiKey", () => {
    createHttpHandler("my-api-key", undefined);

    expect(HttpHandler).toHaveBeenCalledWith(
      "https://api.careevolutionapi.com",
      {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-api-key": "my-api-key",
      },
      120_000,
    );
  });
});
