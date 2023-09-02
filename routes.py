from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db

import schemas
import models

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    if not tasks:
        return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No tasks exist.")
    else:
        return {"tasks": tasks}


@router.get("/{task_id}", status_code=status.HTTP_200_OK)
async def get_task_by(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No task with this id: {task_id} found.")
    else:
        return {"task": task}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(payload: schemas.TaskSchema, db: Session = Depends(get_db)):
    new_task = models.Task(**payload.model_dump())
    del new_task.id
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"task": new_task}


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_by(task_id: int, response: Response, db: Session = Depends(get_db)):
    task_query = db.query(models.Task).filter(models.Task.id == task_id)
    task = task_query.first()
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return HTTPException(detail=f"No task with this id: {task_id} found.")
    else:
        task_query.delete(synchronize_session=False)
        db.commit()
        return {"task": task}


@router.patch("/{task_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task(task_id: int, payload: schemas.TaskSchema, response: Response, db: Session = Depends(get_db)):
    task_query = db.query(models.Task).filter(models.Task.id == task_id)
    task = task_query.first()
    if not task:
        response.status_code = status.HTTP_404_NOT_FOUND
        return HTTPException(detail=f"No task with this id: {task_id} found.")
    else:

        db.commit()
        return {"task": task}
