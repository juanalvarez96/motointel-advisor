from app.domain.motorcycle import Motorcycle, MotorcycleCreate

class InMemoryMotorcycleRepository:
    def __init__(self) -> None:
        self._motorcycles: dict[str, Motorcycle] = {}

    def create(self, payload: MotorcycleCreate) -> Motorcycle:
        data = payload.model_dump()
        motorcycle = Motorcycle(**data)
        self._motorcycles[motorcycle.id] = motorcycle
        return motorcycle
    
    def get(self, motorcycle_id: str) -> Motorcycle | None:
        return self._motorcycles.get(motorcycle_id)
    
    def list(self) -> list[Motorcycle]:
        return list(self._motorcycles.values())
