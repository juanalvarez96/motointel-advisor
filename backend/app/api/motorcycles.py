from fastapi import APIRouter, Depends, status
from app.domain.motorcycle import Motorcycle
from backend.app.api.dependencies import get_motorcycle_repository
from backend.app.repositories.motorcycle_repository import InMemoryMotorcycleRepository
from backend.app.domain.motorcycle import MotorcycleCreate
from backend.app.services.motorcycle_service import MotorcycleService



router = APIRouter()

@router.post(
        "/motorcycles",
        response_model=Motorcycle,
        status_code=status.HTTP_201_CREATED,
)
def create_motorcycle(payload: MotorcycleCreate, repository: InMemoryMotorcycleRepository = Depends(get_motorcycle_repository)) -> Motorcycle:
    service = MotorcycleService(repository)
    return service.create_motorcycle(payload)