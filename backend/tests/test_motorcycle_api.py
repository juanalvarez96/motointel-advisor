import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_motorcycle_repository
from app.main import app
from app.repositories.motorcycle_repository import InMemoryMotorcycleRepository


@pytest.fixture(autouse=True)
def use_fresh_repository():
    repository = InMemoryMotorcycleRepository()

    app.dependency_overrides[get_motorcycle_repository] = lambda: repository

    yield

    app.dependency_overrides.clear()


client = TestClient(app)


def test_create_motorcycle_endpoint() -> None:
    payload = {
        "make": "Honda",
        "model": "CB650R",
        "year": 2025,
        "category": "naked",
    }

    response = client.post("/motorcycles", json=payload)

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["make"] == "Honda"
    assert response_data["model"] == "CB650R"
    assert response_data["id"]


def test_get_motorcycle_endpoint() -> None:
    payload = {
        "make": "Honda",
        "model": "CB650R",
        "year": 2025,
        "category": "naked",
    }

    create_response = client.post("/motorcycles", json=payload)
    created = create_response.json()

    motorcycle_id = created["id"]

    get_response = client.get(f"/motorcycles/{motorcycle_id}")

    assert get_response.status_code == 200

    retrieved = get_response.json()

    assert retrieved["id"] == motorcycle_id
    assert retrieved["make"] == payload["make"]


def test_list_motorcycles_endpoint() -> None:
    payload = {
        "make": "Yamaha",
        "model": "MT-07",
        "year": 2025,
        "category": "naked",
    }

    create_response = client.post("/motorcycles", json=payload)
    created = create_response.json()

    response = client.get("/motorcycles")

    assert response.status_code == 200

    motorcycles = response.json()

    assert isinstance(motorcycles, list)
    assert len(motorcycles) == 1
    assert motorcycles[0]["id"] == created["id"]


def test_get_unknown_motorcycle_returns_404() -> None:
    response = client.get("/motorcycles/unknownd_id")

    assert response.status_code == 404

    response_data = response.json()

    assert response_data["detail"] == "Motorcycle not found"


def test_create_motorcycle_with_invalid_year_returns_422() -> None:
    payload = {
        "make": "Honda",
        "model": "CB650R",
        "year": 8888,
        "category": "naked",
    }

    response = client.post("/motorcycles", json=payload)

    assert response.status_code == 422

    response_data = response.json()
    assert response_data["detail"]


def test_delete_motorcycle_endpoint() -> None:
    payload = {
        "make": "Suzuki",
        "model": "V-Strom 800DE",
        "year": 2025,
        "category": "adventure",
    }

    create_response = client.post("/motorcycles", json=payload)
    motorcycle_id = create_response.json()["id"]

    delete_response = client.delete(f"/motorcycles/{motorcycle_id}")

    assert delete_response.status_code == 204

    get_response = client.get(f"/motorcycles/{motorcycle_id}")

    assert get_response.status_code == 404


def test_delete_unknown_motorcycle_returns_404() -> None:
    response = client.delete("/motorcycles/unknown-id")

    assert response.status_code == 404
    assert response.json()["detail"] == "Motorcycle not found"
