from app.domain.motorcycle import MotorcycleCreate
from app.repositories.motorcycle_repository import InMemoryMotorcycleRepository
from app.services.motorcycle_service import MotorcycleService


def test_service_uses_provided_repository() -> None:
    repository = InMemoryMotorcycleRepository()
    service = MotorcycleService(repository)

    assert service.repository is repository


def test_service_creates_motorcycle() -> None:
    repository = InMemoryMotorcycleRepository()
    service = MotorcycleService(repository)

    payload = MotorcycleCreate(
        make="Honda",
        model="CB650R",
        year=2025,
        category="naked",
    )

    created = service.create_motorcycle(payload)
    returned_motorcycle = service.repository.get(created.id)
    assert returned_motorcycle.id == created.id

def test_service_gets_motorcycle_by_id() -> None:
    repository = InMemoryMotorcycleRepository()
    service = MotorcycleService(repository)

    payload = MotorcycleCreate(
        make="Honda",
        model="CB650R",
        year=2025,
        category="naked",
    )

    created = service.create_motorcycle(payload)
    retrieved_motorcycle = service.get_motorcycle(created.id)
    assert retrieved_motorcycle is not None
    assert retrieved_motorcycle.id == created.id