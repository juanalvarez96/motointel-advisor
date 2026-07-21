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
