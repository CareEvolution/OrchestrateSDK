# Orchestrate SDK

The Orchestrate SDK provides TypeScript, Python, and C# clients for interacting with the Orchestrate API at <https://api.careevolutionapi.com>.

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

C#:

```bash
dotnet add package CareEvolution.Orchestrate
```

## Usage

### TypeScript

```typescript
import { OrchestrateApi } from '@careevolution/orchestrate';

const orchestrate = new OrchestrateApi({apiKey: "your-api-key"});
await orchestrate.terminology.classifyCondition({
  code: "119981000146107",
  system: "SNOMED",
});
```

### Python

```python
from orchestrate import OrchestrateApi

api = OrchestrateApi(api_key="your-api-key")
api.terminology.classify_condition(code="119981000146107", system="SNOMED")
```

### C\#

```csharp
using CareEvolution.Orchestrate;

var api = new OrchestrateApi(new OrchestrateClientOptions
{
    ApiKey = "your-api-key",
});

await api.Terminology.ClassifyConditionAsync(new ClassifyConditionRequest
{
    Code = "119981000146107",
    System = "SNOMED",
});
```

Additionally, C# also supports dependency injection with `IOrchestrateApi` and `OrchestrateApi` registered in the service collection.

```csharp
using CareEvolution.Orchestrate;

var services = new ServiceCollection();
services.AddOrchestrateApi();
```

## Configuration

The SDK supports environment variables for configuring HTTP behavior. These can be used for local development, CI, or shared runtime configuration.

For the primary `OrchestrateApi` clients in TypeScript, Python, and C#:

| Environment variable | Purpose | Default |
| --- | --- | --- |
| `ORCHESTRATE_API_KEY` | Sets the API key sent as the `x-api-key` header. | Not set |
| `ORCHESTRATE_BASE_URL` | Overrides the base URL for Orchestrate API requests. | `https://api.careevolutionapi.com` |
| `ORCHESTRATE_TIMEOUT_MS` | Sets the request timeout in milliseconds. | `120000` |
| `ORCHESTRATE_ADDITIONAL_HEADERS` | Adds extra headers for every request. The value must be a JSON object of string header names to string values. | Not set |

Environment variables used by the identity clients:

| Environment variable | Purpose |
| --- | --- |
| `ORCHESTRATE_IDENTITY_URL` | Base URL for `IdentityApi`. Required unless the URL is passed directly when creating the client. |
| `ORCHESTRATE_IDENTITY_API_KEY` | API key sent as the `x-api-key` header for `IdentityApi`. |
| `ORCHESTRATE_IDENTITY_METRICS_KEY` | Metrics key sent as the `Authorization` header for `IdentityApi`. A value with or without the `Basic` prefix is accepted. |
| `ORCHESTRATE_IDENTITY_LOCAL_HASHING_URL` | Base URL for `LocalHashingApi`. Required unless the URL is passed directly when creating the client. |

### Configuration Precedence

When the same setting is provided in more than one place, the SDK resolves it in this order:

1. Explicit constructor parameters
2. The matching environment variable
3. The SDK default, when one exists

For example, passing `api_key` or `timeout_ms` in Python, `apiKey` or `timeoutMs` in TypeScript, or `ApiKey` or `TimeoutMs` in C# overrides the corresponding environment variable.

`ORCHESTRATE_ADDITIONAL_HEADERS` is additive. It is merged into the request headers before the SDK applies its standard `Accept`, `Content-Type`, authentication, and metrics headers, so the SDK-managed headers take precedence if the same header name is supplied in multiple places.

### Examples

#### TypeScript Example

```bash
export ORCHESTRATE_API_KEY="your-api-key"
export ORCHESTRATE_TIMEOUT_MS="30000"
export ORCHESTRATE_ADDITIONAL_HEADERS='{"x-correlation-id":"demo-run"}'
```

```typescript
import { OrchestrateApi } from '@careevolution/orchestrate';

const orchestrate = new OrchestrateApi();
```

#### Python Example

```bash
export ORCHESTRATE_API_KEY="your-api-key"
export ORCHESTRATE_TIMEOUT_MS="30000"
export ORCHESTRATE_ADDITIONAL_HEADERS='{"x-correlation-id":"demo-run"}'
```

```python
from orchestrate import OrchestrateApi

api = OrchestrateApi()
```

#### C\# Example

With environment values as above or DI configuration:

```csharp
using CareEvolution.Orchestrate;

var services = new ServiceCollection();
services.AddOrchestrateApi(options =>
{
    options.ApiKey = "your-api-key";
    options.TimeoutMs = 30000;
});
```
