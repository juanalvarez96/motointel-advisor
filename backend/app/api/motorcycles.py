from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_motorcycle_repository
from app.domain.motorcycle import Motorcycle, MotorcycleCreate
from app.repositories.motorcycle_repository import InMemoryMotorcycleRepository
from app.services.motorcycle_service import MotorcycleService

router = APIRouter()


@router.post(
    "/motorcycles",
    response_model=Motorcycle,
    status_code=status.HTTP_201_CREATED,
)
def create_motorcycle(
    payload: MotorcycleCreate,
    repository: Annotated[InMemoryMotorcycleRepository, Depends(get_motorcycle_repository)],
) -> Motorcycle:
    service = MotorcycleService(repository)
    return service.create_motorcycle(payload)
