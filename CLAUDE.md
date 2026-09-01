# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Three independent client libraries for the CareEvolution Orchestrate API (`https://api.careevolutionapi.com`): TypeScript (`typescript/`), Python (`python/`), and C# (`dotnet/`). Each is published separately (`@careevolution/orchestrate` on npm, `orchestrate-api` on PyPI, `CareEvolution.Orchestrate` on NuGet). API reference lives at `https://rosetta-api.docs.careevolution.com/`.

The three clients deliberately expose the same surface. A change to one client's public API almost always needs the same change mirrored in the other two, with naming adjusted per language convention (`classifyCondition` / `classify_condition` / `ClassifyConditionAsync`).

## Per-language commands

Run these from the language subdirectory, not the repo root.

TypeScript (`typescript/`):

```bash
npm ci
npm run test          # vitest run, default suite
npm run test:watch
npm run test:e2e      # vitest -c vitest.config.e2e.js
npm run build         # emits ESM + CJS into dist/
npm run fmt           # prettier --check .  (fmt:fix to write)
```

Run a single TS test with `npx vitest run tests/api.test.ts -t "classify condition"`.

Python (`python/`):

```bash
poetry install --with main,test
poetry run pytest             # addopts already apply: -n 4 -m default
poetry run pytest -m e2e
poetry run black --check .    # CI lint gate; drop --check to format
poetry run mypy orchestrate
```

Run a single Python test with `poetry run pytest -n0 tests/test_api.py::test_name` (`-n0` disables xdist so breakpoints and output work).

C# (`dotnet/`):

```bash
dotnet tool restore
dotnet csharpier check .      # CI format gate; `dotnet csharpier format .` to fix
dotnet restore OrchestrateSDK.DotNet.sln
dotnet build OrchestrateSDK.DotNet.sln --configuration Release
dotnet test OrchestrateSDK.DotNet.sln --configuration Release
```

Run a single C# test with `dotnet test --filter "FullyQualifiedName~RouteBuilderTests"`.

## Tests hit the live API

The `default` test suite makes real calls to the Orchestrate API. Tests need a repo-root `.env` file (gitignored, `.env.example` is the template) with at least `ORCHESTRATE_API_KEY`. Python and TypeScript load it with dotenv. C# walks up from the test binary to find it.

Two suites exist, `default` and `e2e`. The `e2e` suite additionally needs the Local Hashing Service running as a Docker container on port 7002, plus the identity variables `ORCHESTRATE_IDENTITY_API_KEY`, `ORCHESTRATE_IDENTITY_METRICS_KEY`, `ORCHESTRATE_IDENTITY_URL`, and `ORCHESTRATE_IDENTITY_LOCAL_HASHING_URL`. See `https://orchestrate.docs.careevolution.com/identity/local_hash/hosting.html` for starting the container.

C# live tests self-skip when their required environment variables are missing or the local service is unreachable (`LiveFactAttribute` / `LiveTheoryAttribute` in `tests/.../Helpers/LiveTestAttributes.cs`). Python and TS tests do not skip, so a missing key surfaces as a failure.

## Architecture

`OrchestrateApi` is the entry point in every language. It composes three sub-clients over one shared HTTP handler: `terminology` (code classification, standardization, FHIR terminology resources), `convert` (format conversion between CDA, HL7v2, FHIR versions, X12, NEMSIS, OMOP, and PDF/HTML), and `insight` (risk profiles).

Identity is a separate client (`IdentityApi`) with its own base URL and a second auth header. It sends `x-api-key` plus `Authorization: Basic <metricsKey>`. `LocalHashingApi` is a third client pointed at the on-prem hashing container. These are not reachable from `OrchestrateApi`.

Configuration resolves in a fixed precedence: explicit constructor argument, then environment variable, then built-in default. The resolution logic is centralized per language in `typescript/src/httpHandlerFactory.ts`, `python/orchestrate/_internal/http_handler.py`, and `dotnet/src/CareEvolution.Orchestrate/EnvironmentConfiguration.cs`. `ORCHESTRATE_ADDITIONAL_HEADERS` (a JSON object) is merged in first, so SDK-managed headers win on conflict.

The HTTP handler is a thin wrapper over `fetch` / `requests` / `HttpClient`. On error responses it parses FHIR `OperationOutcome` and RFC 9110 problem+json bodies into the library's exception types (`exceptions.ts`, `orchestrate/_internal/exceptions.py`).

Batch overloading: many `terminology` and `convert` methods accept either a single request object or an array. An array is rerouted to `{path}/batch` wrapped as `{ items: [...] }` and unwrapped from the response's `items`. See `typescript/src/batch.ts` and `python/orchestrate/_internal/batch.py`.

Response bodies are typed as FHIR R4 resources, via `@types/fhir` in TypeScript, `CareEvolution.Fhir.Core` in C#, and the `orchestrate.fhir` module in Python.

### Language-specific notes

Python: everything public re-exports from `orchestrate._internal.*`. Treat `_internal` as private and unstable. Public modules are `terminology`, `insight`, `convert`, `exceptions`, `identity`, `fhir`.

TypeScript: the build produces both ESM (`tsconfig.esm.json`) and CJS (`tsconfig.cjs.json` plus `scripts/build-cjs-package.mjs`). `package.json` declares subpath exports (`@careevolution/orchestrate/terminology`, `/identity`, etc.) that must stay in sync with `src/` module names.

C#: `OrchestrateApi` and `IdentityApi` take an `HttpClient` in their constructor for DI and testability. `services.AddOrchestrateApi()` registers `IOrchestrateApi` against a named `IHttpClientFactory` client. Targets `net8.0` and `net10.0`.

## Releases

Version is `0.0.0` in all source. The real version is injected at publish time from the git tag. Pushing a tag to `main` triggers `.github/workflows/deploy.yml`, which runs the full test suite (TypeScript, then Python, then C#, sequentially) and publishes to npm, PyPI, and NuGet. `workflow_dispatch` runs produce dev builds to internal ProGet and TestPyPI instead.

Contribute by forking from `main` and opening a PR back into it. The PR template (`.github/pull_request_template.md`) carries a security checklist on the premise that all file contents are public, plus a Change Control Board approval section.
