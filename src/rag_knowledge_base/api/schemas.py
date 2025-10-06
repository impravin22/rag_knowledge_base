from __future__ import annotations

from typing import Any, Dict, List
from pydantic import BaseModel, Field


class RunRequest(BaseModel):
    model_name: str = Field(default="dummy")
    payload: Dict[str, Any]


class RunResponse(BaseModel):
    ok: bool
    model: str
    received: List[str]
