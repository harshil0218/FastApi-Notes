from fastapi import APIRouter, HTTPException, status
from .. import models
from ..schemas import UserBase
from ..database import db_dependency

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    
    # Create a new user
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Refresh to get the full data from the database

    return db_user

@router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: db_dependency):
    
    # Get a user by ID
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    
    return user