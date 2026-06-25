import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_health_endpoint_returns_healthy(client: AsyncClient):
    response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


@pytest.mark.anyio
async def test_healthy_alias_returns_same_payload(client: AsyncClient):
    response = await client.get("/healthy")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
