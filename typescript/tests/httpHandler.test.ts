import { describe, it, expect, vi } from "vitest";
import { HttpHandler } from "../src/httpHandler";
import { createHttpHandler } from "../src/httpHandlerFactory";

vi.mock("../src/httpHandler");

describe("createHttpHandler", () => {
  it("should create an HttpHandler with the correct baseUrl and apiKey", () => {
    const baseUrl = "http://example.com";
    const apiKey = "12345";

    createHttpHandler(baseUrl, apiKey, {});

    expect(HttpHandler).toHaveBeenCalledWith(baseUrl, {
      "Content-Type": "application/json",
      Accept: "application/json",
      "x-api-key": apiKey,
    });
  });
});
