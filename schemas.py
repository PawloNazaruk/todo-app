
# Schemas of Tasks objects used by TODO app

from datetime import datetime
from typing import List
from pydantic import BaseModel

from models import Priority


class TaskSchema(BaseModel):
    id: int = None
    title: str
    content: str = None
    priority: Priority
    category: str = None
    completed: str = None  # czy lepiej 0?
    createdAt: datetime
    updatedAt: datetime
    finishUntil: datetime
    completedAt: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
