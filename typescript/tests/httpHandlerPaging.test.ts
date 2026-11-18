import { afterEach, describe, expect, it, vi } from "vitest";
import { HttpHandler } from "../src/httpHandler";

afterEach(() => vi.unstubAllGlobals());

describe("paging link requests", () => {
  it.each(["/continuation?cursor=a%2Bb", "https://api.example.test/continuation?cursor=a%2Bb"])(
    "fetches %s with the existing authentication",
    async (path) => {
      const fetch = vi.fn().mockResolvedValue(new Response(JSON.stringify({ resourceType: "Bundle" })));
      vi.stubGlobal("fetch", fetch);
      const handler = new HttpHandler("https://api.example.test", { "x-api-key": "test-key" }, 0);
      expect(await handler.get(path)).toEqual({ resourceType: "Bundle" });
      expect(fetch).toHaveBeenCalledWith(
        "https://api.example.test/continuation?cursor=a%2Bb",
        expect.objectContaining({ headers: { "x-api-key": "test-key" } }),
      );
    },
  );
  it.each(["https://other.example/next", "http://api.example.test/next"])(
    "rejects another origin %s before HTTP",
    async (path) => {
      const fetch = vi.fn();
      vi.stubGlobal("fetch", fetch);
      const handler = new HttpHandler("https://api.example.test", { "x-api-key": "test-key" }, 0);
      await expect(handler.get(path)).rejects.toThrow("Paging links must use the configured API origin");
      expect(fetch).not.toHaveBeenCalled();
    },
  );
});
