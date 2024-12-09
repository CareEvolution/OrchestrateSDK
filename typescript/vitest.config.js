import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    testTimeout: 20000,
    exclude: ["tests/identity/*.test.ts", "node_modules/**/*"]
  },
});
