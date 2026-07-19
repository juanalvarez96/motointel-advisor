from fastapi import APIRouter, Depends, status
from app.domain.motorcycle import Motorcycle



router = APIRouter()

@router.post(
        "/motorcycles",
        response_model=Motorcycle,
        status_code=201,
)
def create_motorcycle():
    raise NotImplemented()
