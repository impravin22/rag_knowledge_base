import pytest
from httpx import AsyncClient
from rag_knowledge_base.app import app


@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/api/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "ok"


@pytest.mark.asyncio
async def test_run():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post("/api/run", json={"model_name": "m", "payload": {"a": 1}})
        assert r.status_code == 200
        data = r.json()
        assert data["ok"] is True
        assert data["model"] == "m"
        assert "a" in data["received"]
