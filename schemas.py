from datetime import datetime
from typing import List
from pydantic import BaseModel

from models import Priority


class TaskSchema(BaseModel):
    id: int = None
    title: str
    content: str = None
    priority: str = None
    category: str = None
    completed: bool = None  # czy lepiej 0?
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListTasks(BaseModel):
    status: str
    results: int
    notes: List[TaskSchema]
