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

When passing in your Orchestrate API key, you can either specify it during creation of the client or by setting the `ORCHESTRATE_API_KEY` environment variable.

TypeScript:

```typescript
import { OrchestrateApi } from '@careevolution/orchestrate';

process.env.ORCHESTRATE_API_KEY = "your-api-key";

const orchestrate = new OrchestrateApi();
await orchestrate.terminology.classifyCondition({
  code: "119981000146107",
  system: "SNOMED",
});
```

Python:

```python
import os
from orchestrate import OrchestrateApi

os.environ["ORCHESTRATE_API_KEY"] = "your-api-key"

api = OrchestrateApi()
api.terminology.classify_condition(code="119981000146107", system="SNOMED")
```
