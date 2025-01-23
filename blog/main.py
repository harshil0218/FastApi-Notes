from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel

from . import models
from .database import engine, SessionLocal
from .router import blog, user
from .schemas import BlogBase, UserBase  # Add a response schema for clarity

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
# Dependency for getting the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()




# @app.post('/blogs/', status_code=status.HTTP_201_CREATED)
# async def create_blog(blog: BlogBase, db: db_dependency):
    
#     # Create a new blog
#     db_blog = models.Blog(title=blog.title, body=blog.body, published=blog.published, user_id=blog.user_id)
#     db.add(db_blog)
#     db.commit()
#     db.refresh(db_blog)

#     return db_blog

# @app.get('/blogs/{blog_id}', status_code=status.HTTP_200_OK)
# async def get_blog(blog_id: int, db: db_dependency):
    
#     # Get a blog by ID
#     blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
#     if blog is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    
#     return blog

# @app.get('/blogs/', status_code=status.HTTP_200_OK)
# async def get_blogs(db: db_dependency):
    
#     # Get all blogs
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.delete('/blogs/{blog_id}', status_code=status.HTTP_200_OK)
# async def delete_blog(blog_id: int, db: db_dependency):
    
#     # Delete a blog by ID
#     blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
#     if blog is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    
#     db.delete(blog)
#     db.commit()
    
#     return {'message': 'Blog deleted successfully'}


# @app.post('/users/', status_code=status.HTTP_201_CREATED)
# async def create_user(user: UserBase, db: db_dependency):
    
#     # Create a new user
#     db_user = models.User(name=user.name)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)  # Refresh to get the full data from the database

#     return db_user

# @app.get('/users/{user_id}', status_code=status.HTTP_200_OK)
# async def get_user(user_id: int, db: db_dependency):
    
#     # Get a user by ID
#     user = db.query(models.User).filter(models.User.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    
#     return user