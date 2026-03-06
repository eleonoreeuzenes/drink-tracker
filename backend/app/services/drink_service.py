# app.services.drink_service.py

from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.models import Drink, DrinkEvent
from app.schemas.schemas import DrinkCreate, DrinkEventCreate


def create_drink(db: Session, drink: DrinkCreate) -> Drink:
    db_drink = Drink(name=drink.name)
    db.add(db_drink)
    db.commit()
    db.refresh(db_drink)
    if not db_drink:
        raise ValueError("Failed to create drink")
    return db_drink

def get_drink(db: Session, drink_id: int) -> Drink:
    drink = db.query(Drink).filter(Drink.id == drink_id).first()
    if not drink:
        raise ValueError("Drink not found")
    return drink

def create_drink_event(db: Session, event: DrinkEventCreate) -> DrinkEvent:
    drink = get_drink(db, event.drink_id)
    if not drink:
        raise ValueError("Drink not found for event")
    
    db_event = DrinkEvent(drink_id=event.drink_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_drink_total_events(db: Session, drink_id: int) -> int:
    total = db.query(DrinkEvent).filter(DrinkEvent.drink_id == drink_id).count()
    if total is None:
        raise ValueError("Drink not found for counting events")
    return total

def get_daily_drink_events(db: Session, drink_id: int) -> list[DrinkEvent]:
    now = datetime.now(timezone.utc)
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    events = db.query(DrinkEvent).filter(
        DrinkEvent.drink_id == drink_id,
        DrinkEvent.timestamp >= start_of_day
    ).all()
    if events is None:
        raise ValueError("Drink not found for daily events")
    return events