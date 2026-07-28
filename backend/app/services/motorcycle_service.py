from app.domain.motorcycle import Motorcycle, MotorcycleCreate, MotorcycleUpdate
from app.repositories.base import MotorcycleRepository


class MotorcycleService:
    def __init__(self, repository: MotorcycleRepository) -> None:
        self.repository = repository

    def create_motorcycle(self, payload: MotorcycleCreate) -> Motorcycle:
        return self.repository.create(payload)

    def get_motorcycle(self, motorcycle_id: str) -> Motorcycle | None:
        return self.repository.get(motorcycle_id)

    def list_motorcycles(self) -> list[Motorcycle]:
        return self.repository.list()

    def delete_motorcycle(self, motorcycle_id: str) -> bool:
        return self.repository.delete(motorcycle_id)

    def update_motorcycle(self, motorcycle_id: str, payload: MotorcycleUpdate) -> Motorcycle | None:
        return self.repository.update(motorcycle_id, payload)
