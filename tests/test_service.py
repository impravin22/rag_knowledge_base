import pytest
from rag_knowledge_base import Service

@pytest.mark.asyncio
async def test_service_runs():
    svc = Service(model_name="test-model")
    result = await svc.run({"a": 1})
    assert result["ok"] is True
    assert result["model"] == "test-model"
