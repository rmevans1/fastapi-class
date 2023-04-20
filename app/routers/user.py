from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import db_user
from app.db.database import get_db
from app.schemas.schemas import UserBase, UserDisplay

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Create User
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read All Users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read One User

# Update User

# Delete User