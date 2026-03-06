# app/schemas/schemas.py
from datetime import datetime

from backend.app.models.models import DrinkEvent
from pydantic import BaseModel


# --- DrinkEvent schemas ---
class DrinkEventBase(BaseModel):
    drink_id: int

class DrinkEventCreate(BaseModel):
    pass  

class DrinkEventResponse(BaseModel):
    id: int
    drink_id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# --- Drink schemas ---
class DrinkCreate(BaseModel):
    name: str

class DrinkResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class DrinkWithEvents(BaseModel):
    id: int
    name: str
    events: list[DrinkEventResponse] = []

    class Config:
        from_attributes = True
