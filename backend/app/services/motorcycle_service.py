from app.domain.motorcycle import Motorcycle, MotorcycleCreate
from app.repositories.motorcycle_repository import InMemoryMotorcycleRepository


class MotorcycleService:
    def __init__(self, repository: InMemoryMotorcycleRepository) -> None:
        self.repository = repository

    def create_motorcycle(self, payload: MotorcycleCreate) -> Motorcycle:
        return self.repository.create(payload)

    def get_motorcycle(self, motorcycle_id: str) -> Motorcycle | None:
        return self.repository.get(motorcycle_id)

    def list_motorcycles(self) -> list[Motorcycle]:
        return self.repository.list()
