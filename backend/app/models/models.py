from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    events = relationship("DrinkEvent", back_populates="drink")

class DrinkEvent(Base):
    __tablename__ = "drink_events"

    id = Column(Integer, primary_key=True, index=True)
    drink_id = Column(Integer, ForeignKey("drinks.id"), nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    drink = relationship("Drink", back_populates="events")
