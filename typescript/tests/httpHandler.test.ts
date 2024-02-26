import { describe, it, expect, vi } from "vitest";
import { HttpHandler } from "../src/httpHandler";
import { createHttpHandler } from "../src/httpHandlerFactory";

vi.mock("../src/httpHandler");

describe("createHttpHandler", () => {
  it("should create an HttpHandler defaulted to api.careevolutionapi.com", () => {

    createHttpHandler(undefined);

    expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
    });
  });

  it("should prefer the the environment variable", () => {
    try {
      vi.stubEnv("ORCHESTRATE_BASE_URL", "https://env.example.com");

      createHttpHandler(undefined);

      expect(HttpHandler).toHaveBeenCalledWith("https://env.example.com", {
        "Content-Type": "application/json",
        Accept: "application/json",
      });
    } finally {
      vi.unstubAllEnvs();
    }
  });

  it("should create an HttpHandler with the provided apiKey", () => {
    createHttpHandler("my-api-key");

    expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
      "x-api-key": "my-api-key",
    });
  });

  it("should prefer the api key parameter over the environment variable", () => {
    try {
      vi.stubEnv("ORCHESTRATE_API_KEY", "env-api-key");

      createHttpHandler("my-api-key");

      expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-api-key": "my-api-key",
      });
    } finally {
      vi.unstubAllEnvs();
    }
  });

  it("should use api key environment variable if no parameter is provided", () => {
    try {
      vi.stubEnv("ORCHESTRATE_API_KEY", "env-api-key");

      createHttpHandler(undefined);

      expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-api-key": "env-api-key",
      });
    } finally {
      vi.unstubAllEnvs();
    }
  });

  it("should create an HttpHandler with the provided additional headers", () => {
    try {
      vi.stubEnv("ORCHESTRATE_ADDITIONAL_HEADERS", JSON.stringify({ "x-custom-header": "custom-value" }));

      createHttpHandler(undefined);

      expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
        "Content-Type": "application/json",
        Accept: "application/json",
        "x-custom-header": "custom-value",
      });
    } finally {
      vi.unstubAllEnvs();
    }
  });
});