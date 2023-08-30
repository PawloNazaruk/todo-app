
# Routes of endpoints

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db

import schemas
import models

router = APIRouter()


@router.get("/")
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task)
    return {"status": 'success', "results": len(tasks), "tasks": tasks}
