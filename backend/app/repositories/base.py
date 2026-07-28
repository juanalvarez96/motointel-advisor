from typing import Protocol

from app.domain.motorcycle import (
    Motorcycle,
    MotorcycleCreate,
    MotorcycleUpdate,
)


class MotorcycleRepository(Protocol):
    def create(self, payload: MotorcycleCreate) -> Motorcycle: ...

    def get(self, motorcycle_id: str) -> Motorcycle | None: ...

    def list(self) -> list[Motorcycle]: ...

    def update(
        self,
        motorcycle_id: str,
        payload: MotorcycleUpdate,
    ) -> Motorcycle | None: ...

    def delete(self, motorcycle_id: str) -> bool: ...
