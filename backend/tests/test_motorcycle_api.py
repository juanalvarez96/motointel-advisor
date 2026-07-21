from fastapi.testclient import TestClient

from app.main import app

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
    assert any(motorcycle["id"] == created["id"] for motorcycle in motorcycles)


def test_get_unknown_motorcycle_returns_404() -> None:
    response = client.get("/motorcycles/unknownd_id")

    assert response.status_code == 404

    response_data = response.json()

    assert response_data["detail"] == "Motorcycle not found"
