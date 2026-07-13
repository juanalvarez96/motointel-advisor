from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

MotorcycleCategory = Literal[
    "adventure",
    "sport",
    "naked",
    "touring",
    "cruiser",
    "scooter",
    "enduro",
    "trail",
    "unknown",
]


class MotorcycleCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    make: str = Field(..., min_length=1, examples=["Yamaha"])
    model: str = Field(..., min_length=1, examples=["Ténéré 700"])
    year: int = Field(..., ge=1900, le=2100, examples=[2025])
    category: MotorcycleCategory = "unknown"
    engine_cc: int | None = Field(default=None, ge=1, examples=[689])
    power_hp: float | None = Field(default=None, ge=0, examples=[72.0])
    weight_kg: float | None = Field(default=None, ge=0, examples=[205.0])
    seat_height_mm: int | None = Field(default=None, ge=0, examples=[875])
    features: list[str] = Field(default_factory=list)
    description: str | None = None


class Motorcycle(MotorcycleCreate):
    id: str = Field(default_factory=lambda: str(uuid4()))
