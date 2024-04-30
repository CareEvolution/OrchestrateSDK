import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    testTimeout: 300000,
    hookTimeout: 300000,
    exclude: ["tests/identity/*.test.ts", "node_modules/**/*"]
  },
});
