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
