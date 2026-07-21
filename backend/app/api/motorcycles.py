from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

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


@router.get(
    "/motorcycles/{motorcycle_id}",
    response_model=Motorcycle,
)
def get_motorcycle(
    motorcycle_id: str,
    repository: Annotated[
        InMemoryMotorcycleRepository,
        Depends(get_motorcycle_repository),
    ],
) -> Motorcycle:
    service = MotorcycleService(repository)

    motorcycle = service.get_motorcycle(motorcycle_id)

    if motorcycle is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Motorcycle not found",
        )

    return motorcycle


@router.get(
    "/motorcycles",
    response_model=list[Motorcycle],
)
def list_motorcycles(
    repository: Annotated[
        InMemoryMotorcycleRepository,
        Depends(get_motorcycle_repository),
    ],
) -> list[Motorcycle]:
    service = MotorcycleService(repository)

    return service.list_motorcycles()
