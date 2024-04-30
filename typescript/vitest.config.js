import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    exclude: ["tests/identity/*.test.ts", "node_modules/**/*"]
  },
});
