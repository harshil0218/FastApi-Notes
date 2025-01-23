from fastapi import APIRouter, HTTPException, status
from .. import models
from ..schemas import BlogBase
from ..database import db_dependency

router = APIRouter(
    prefix='/blogs',
    tags=['blogs'],
)
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_blog(blog: BlogBase, db: db_dependency):
    
    # Create a new blog
    db_blog = models.Blog(title=blog.title, body=blog.body, published=blog.published, user_id=blog.user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)

    return db_blog

@router.get('/{blog_id}', status_code=status.HTTP_200_OK)
async def get_blog(blog_id: int, db: db_dependency):
    
    # Get a blog by ID
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    
    return blog

@router.get('/', status_code=status.HTTP_200_OK)
async def get_blogs(db: db_dependency):
    
    # Get all blogs
    blogs = db.query(models.Blog).all()
    return blogs

@router.delete('/{blog_id}', status_code=status.HTTP_200_OK)
async def delete_blog(blog_id: int, db: db_dependency):
    
    # Delete a blog by ID
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    
    db.delete(blog)
    db.commit()
    
    return {'message': 'Blog deleted successfully'}