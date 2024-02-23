import { describe, it, expect, vi } from "vitest";
import { HttpHandler } from "../src/httpHandler";
import { createHttpHandler } from "../src/httpHandlerFactory";

vi.mock("../src/httpHandler");

describe("createHttpHandler", () => {
  it("should create an HttpHandler defaulted to api.careevolutionapi.com", () => {

    createHttpHandler(undefined, undefined, undefined);

    expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
    });
  });

  it("should create an HttpHandler with the provided baseUrl", () => {
    createHttpHandler("https://api.example.com", undefined, undefined);

    expect(HttpHandler).toHaveBeenCalledWith("https://api.example.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
    });
  });

  it("should prefer the provided baseUrl over the environment variable", () => {
    try {
      vi.stubEnv("ORCHESTRATE_BASE_URL", "https://env.example.com");

      createHttpHandler("https://argument.example.com", undefined, undefined);

      expect(HttpHandler).toHaveBeenCalledWith("https://argument.example.com", {
        "Content-Type": "application/json",
        Accept: "application/json",
      });
    } finally {
      vi.unstubAllEnvs();
    }
  });

  it("should create an HttpHandler with the provided apiKey", () => {
    createHttpHandler(undefined, "my-api-key", undefined);

    expect(HttpHandler).toHaveBeenCalledWith("https://api.careevolutionapi.com", {
      "Content-Type": "application/json",
      Accept: "application/json",
      "x-api-key": "my-api-key",
    });
  });
});