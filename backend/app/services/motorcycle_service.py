from app.repositories.motorcycle_repository import InMemoryMotorcycleRepository


class MotorcycleService:
    def __init__(self, repository: InMemoryMotorcycleRepository) -> None:
        self.repository = repository
