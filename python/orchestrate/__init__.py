from importlib import metadata
from orchestrate._internal.api import OrchestrateApi

__version__ = metadata.version("orchestrate-api")

__all__ = ["OrchestrateApi"]
