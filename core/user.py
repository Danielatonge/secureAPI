from fastapi import APIRouter, Depends, Response, status 
from sqlalchemy.orm import Session
from schema import schemas
from models import models
from database import configuration
from typing import List, Optional
from api import user

router = APIRouter(tags=["Users"], prefix="/users")
get_db = configuration.get_db


# Create User
@router.post("/", response_model=schemas.ShowUser, 
status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


# Get Users
@router.get("/", response_model=List[schemas.ShowUser], 
status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return user.get_all(db)


# Get Users using the ID
@router.get("/{id}", response_model=Optional[schemas.ShowUser], 
status_code=status.HTTP_200_OK)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)