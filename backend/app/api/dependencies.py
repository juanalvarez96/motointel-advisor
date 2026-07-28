from app.repositories.motorcycle_repository import InMemoryMotorcycleRepository

motorcycle_repository = InMemoryMotorcycleRepository()


def get_motorcycle_repository() -> InMemoryMotorcycleRepository:
    return motorcycle_repository
