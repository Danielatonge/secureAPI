from schema.oa2 import get_current_user
from fastapi import APIRouter, Depends, Response, status 
from sqlalchemy.orm import Session
from schema import schemas
from models import models
from database import configuration
from typing import List, Optional
from api import blog

router = APIRouter(tags=["Blogs"], prefix="/blog")
get_db = configuration.get_db


@router.post("/", response_model=schemas.ShowBlog, 
status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


# Get Blogs
@router.get("/", response_model=List[schemas.ShowBlog], 
status_code=status.HTTP_200_OK)
def get_all_blogs(db: Session = Depends(get_db), 
current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


# Get Blog using the ID
@router.get("/{id}", response_model=Optional[schemas.ShowBlog], 
status_code=status.HTTP_200_OK)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    return blog.show(id, db)


# Delete Blog using the ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)


# Update Blog using the ID
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)