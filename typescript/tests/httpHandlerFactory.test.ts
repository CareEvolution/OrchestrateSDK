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
    createHttpHandler(undefined);

    expect(HttpHandler).toHaveBeenCalledWith("https://env.example.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
      "x-api-key": "env-api-key",
      "x-custom-header": "custom-value",
    });
  });

  it("should prefer the api key parameter over the environment variable", () => {
    createHttpHandler("my-api-key");

    expect(HttpHandler).toHaveBeenCalledWith("https://env.example.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
      "x-api-key": "my-api-key",
      "x-custom-header": "custom-value",
    });
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
    createHttpHandler(undefined);

    expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
      "x-api-key": "env-api-key",
    });
  });

  it("should prefer the api key parameter over the environment variable", () => {
    createHttpHandler("my-api-key");

    expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
      "x-api-key": "my-api-key",
    });
  });

  afterAll(() => {
    vi.unstubAllEnvs();
  });
});


describe("createHttpHandler no environment", () => {
  it("should create an HttpHandler defaulted to api.careevolutionapi.com", () => {
    createHttpHandler(undefined);

    expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
    });
  });

  it("should create an HttpHandler with the provided apiKey", () => {
    createHttpHandler("my-api-key");

    expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
      "x-api-key": "my-api-key",
    });
  });
});
