from __future__ import annotations

import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class Service:
    """Core service with single responsibility operations.

    This class encapsulates the domain logic for the project. It favors
    small, typed methods with explicit responsibilities.
    """

    def __init__(self, model_name: str = "dummy") -> None:
        self.model_name = model_name
        self._initialized: bool = False

    async def initialize(self) -> None:
        """Initialize heavy resources.

        Why: defer expensive setup until the service is actually used
        (keeps startup fast and supports DI/testing).
        """
        self._initialized = True

    async def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process a request and return a structured response.

        Args:
            payload: Input parameters for processing

        Returns:
            A dict with result metadata
        """
        if not self._initialized:
            await self.initialize()

        logger.info("processing request", extra={"keys": list(payload.keys())})
        return {"ok": True, "model": self.model_name, "input_keys": list(payload.keys())}
