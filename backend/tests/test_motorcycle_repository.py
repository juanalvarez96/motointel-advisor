from app.domain.motorcycle import Motorcycle, MotorcycleCreate, MotorcycleUpdate
from app.repositories.motorcycle_repository import InMemoryMotorcycleRepository


def test_repository_creates_motorcycle() -> None:
    repo = InMemoryMotorcycleRepository()
    motorcycle_data = {
        "make": "KTM",
        "model": "Duke 390",
        "year": 2023,
    }

    motorcycle_create = MotorcycleCreate(**motorcycle_data)
    motorcycle = repo.create(motorcycle_create)

    assert isinstance(motorcycle, Motorcycle)
    assert motorcycle.id
    for field_name, expected_value in motorcycle_data.items():
        assert getattr(motorcycle, field_name) == expected_value


def test_repository_gets_motorcycle_by_id() -> None:
    repo = InMemoryMotorcycleRepository()

    payload = MotorcycleCreate(make="KTM", model="Duke 390", year=2023)
    created_motorcycle = repo.create(payload)
    motorcycle_id = created_motorcycle.id

    retrieved_motorcycle = repo.get(motorcycle_id)
    none_id = repo.get("abcdex")
    assert none_id is None
    assert retrieved_motorcycle is not None
    assert retrieved_motorcycle.id == motorcycle_id


def test_repository_lists_motorcycles() -> None:
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

    actual_motorcycle = {
        (motorcycle.make, motorcycle.model, motorcycle.year) for motorcycle in motorcycles
    }

    assert actual_motorcycle == set(expected_motorcycles)


def test_delete_motorcycle() -> None:
    repository = InMemoryMotorcycleRepository()
    motorcycle = repository.create(
        MotorcycleCreate(
            make="Suzuki",
            model="V-Strom 800DE",
            year=2025,
            category="adventure",
        )
    )

    deleted = repository.delete(motorcycle.id)

    assert deleted is True
    assert repository.get(motorcycle.id) is None


def test_motorcycle_update() -> None:
    repository = InMemoryMotorcycleRepository()
    motorcycle = repository.create(
        MotorcycleCreate(
            make="Suzuki",
            model="V-Strom 800DE",
            year=2025,
            category="adventure",
            weight_kg=6473,
        )
    )
    motorcycle = repository.update(
        motorcycle.id,
        MotorcycleUpdate(weight_kg=209),
    )
    assert repository.get(motorcycle.id).weight_kg == 209
