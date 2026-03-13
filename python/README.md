# Orchestrate SDK

The Orchestrate SDK is a TypeScript and JavaScript library for interacting with the Orchestrate API at <https://api.careevolutionapi.com>.

Full documentation of the API is available at <https://rosetta-api.docs.careevolution.com/>.

## Installation

TypeScript:

```bash
npm install @careevolution/orchestrate
```

Python:

```bash
pip install orchestrate-api
```

## Usage

TypeScript:

```typescript
import { OrchestrateApi } from '@careevolution/orchestrate';

const orchestrate = new OrchestrateApi({apiKey: "your-api-key"});
await orchestrate.terminology.classifyCondition({
  code: "119981000146107",
  system: "SNOMED",
});
```

Python:

```python
from orchestrate import OrchestrateApi

api = OrchestrateApi(api_key="your-api-key")
api.terminology.classify_condition(code="119981000146107", system="SNOMED")
```

## Configuration

The Python SDK supports environment variables for configuring HTTP behavior. These can be used to keep credentials and endpoint configuration outside application code.

For `OrchestrateApi`:

| Environment variable | Purpose | Default |
| --- | --- | --- |
| `ORCHESTRATE_API_KEY` | Sets the API key sent as the `x-api-key` header. | Not set |
| `ORCHESTRATE_BASE_URL` | Overrides the base URL for Orchestrate API requests. | `https://api.careevolutionapi.com` |
| `ORCHESTRATE_TIMEOUT_MS` | Sets the request timeout in milliseconds. | `120000` |
| `ORCHESTRATE_ADDITIONAL_HEADERS` | Adds extra headers for every request. The value must be a JSON object of string header names to string values. | Not set |

For the identity APIs:

| Environment variable | Purpose |
| --- | --- |
| `ORCHESTRATE_IDENTITY_URL` | Base URL for `orchestrate.identity.IdentityApi`. Required unless `url` is passed to the constructor. |
| `ORCHESTRATE_IDENTITY_API_KEY` | API key sent as the `x-api-key` header for `orchestrate.identity.IdentityApi`. |
| `ORCHESTRATE_IDENTITY_METRICS_KEY` | Metrics key sent as the `Authorization` header for `orchestrate.identity.IdentityApi`. A value with or without the `Basic ` prefix is accepted. |
| `ORCHESTRATE_IDENTITY_LOCAL_HASHING_URL` | Base URL for `orchestrate.identity.LocalHashingApi`. Required unless `url` is passed to the constructor. |

### Configuration Precedence

When the same setting is supplied in multiple places, the Python SDK resolves it in this order:

1. Explicit constructor parameters
2. The matching environment variable
3. The SDK default, when one exists

For example, `OrchestrateApi(api_key="...")` overrides `ORCHESTRATE_API_KEY`, and `OrchestrateApi(timeout_ms=30000)` overrides `ORCHESTRATE_TIMEOUT_MS`.

`ORCHESTRATE_ADDITIONAL_HEADERS` is additive. It is merged into the request headers before the SDK applies its standard `Accept`, `Content-Type`, authentication, and metrics headers, so SDK-managed headers take precedence if the same header name is supplied in multiple places.

### Examples

```bash
export ORCHESTRATE_API_KEY="your-api-key"
export ORCHESTRATE_TIMEOUT_MS="30000"
export ORCHESTRATE_ADDITIONAL_HEADERS='{"x-correlation-id":"demo-run"}'
```

```python
from orchestrate import OrchestrateApi
from orchestrate.identity import IdentityApi, LocalHashingApi

orchestrate = OrchestrateApi()
identity = IdentityApi()
local_hashing = LocalHashingApi()
```
