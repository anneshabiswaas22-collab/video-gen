import webConfig from "./apps/web/eslint.config.mjs";

export default [
  ...webConfig,
  { settings: { next: { rootDir: "apps/web/" } } },
  { ignores: ["AnalyseFuture/**", ".venv/**", "node_modules/**", "apps/web/.next/**"] },
];
