from app.domain.motorcycle import Motorcycle, MotorcycleCreate

class InMemoryMotorcycleRepository:
    def __init__(self) -> None:
        self._motorcycles: dict[str, Motorcycle] = {}
    def create(self, payload: MotorcycleCreate) -> Motorcycle:
        raise NotImplementedError("This method is not implemented yet.")
    
    def get(self, motorcycle_id: str) -> Motorcycle | None:
        raise NotImplementedError("This method is not implemented yet.")
    
    def list(self) -> list[Motorcycle]:
        raise NotImplementedError("This method is not implemented yet.")
