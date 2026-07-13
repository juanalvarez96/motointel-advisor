from app.domain.motorcycle import Motorcycle, MotorcycleCreate
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

def test_repository_gets_motorcycle_by_id():
    repo = InMemoryMotorcycleRepository()

    payload = MotorcycleCreate(make="KTM", model="Duke 390", year=2023)
    created_motorcycle = repo.create(payload)
    id = created_motorcycle.id

    retrieved_motorcycle = repo.get(id)
    assert retrieved_motorcycle is not None
    assert retrieved_motorcycle.id == id

def test_repository_lists_motorcycles():
    repo = InMemoryMotorcycleRepository()

    payload1 = MotorcycleCreate(make="KTM", model="Duke 390", year=2023)
    payload2 = MotorcycleCreate(make="Yamaha", model="R1", year=2022)

    repo.create(payload1)
    repo.create(payload2)

    motorcycles = repo.list()
    expected_motorcycles = [
        ("KTM", "Duke 390", 2023),
        ("Yamaha", "R1", 2022),
    ]

    assert [(motorcycle.make, motorcycle.model, motorcycle.year) 
            for motorcycle in motorcycles] == expected_motorcycles
    