from sqlalchemy.orm import Session
from schema import schemas
from models import models
from fastapi import HTTPException, status

def get_all(db: Session):
    return db.query(models.Blog).all()

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title,body=request.body, 
    user_id=1)
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
        detail=f"Blog with id {id} not found")
    return blog

def destroy(id: int, db: Session):
    blog_to_delete = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_to_delete.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
        detail=f"Blog with id {id} not found")
    blog_to_delete.delete(synchronize_session=False)
    db.commit()
    return "Delete Successfully"

def update(id:int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
        detail=f"Blog with id {id} not found")
    
    blog.update(request.__dict__)
    db.commit()
    return "Update Successfully"