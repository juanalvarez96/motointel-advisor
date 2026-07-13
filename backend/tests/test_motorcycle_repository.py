from app.domain.motorcycle import MotorcycleCreate, Motorcycle
from app.repositories.motorcycle_repository import InMemoryMotorcycleRepository

def test_repository_creates_motorcycle():
    repo = InMemoryMotorcycleRepository()
    motorcycle_data = {
        "make": "KTM",
        "model": "Duke 390",
        "year": 2023,
    }

    motorcycle_create = MotorcycleCreate(**motorcycle_data)
    motorcycle = repo.create(motorcycle_create)

    assert isinstance(motorcycle, Motorcycle)
    assert motorcycle.id is not None
    for field_name, expected_value in motorcycle_data.items():
        assert getattr(motorcycle, field_name) == expected_value