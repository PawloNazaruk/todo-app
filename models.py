from enum import Enum

from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer, BigInteger
from sqlalchemy.sql import func


class Priority(Enum):
    HIGH: str = "high"
    MEDIUM: str = "medium"
    LOW: str = "low"


class Completed(Enum):
    IN_PROGRESS = 0
    FINISHED = 1


class Task(Base):
    __tablename__ = "tasks"
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    priority = Column(String, nullable=False)
    category = Column(String, nullable=True)
    completed = Column(Boolean, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
