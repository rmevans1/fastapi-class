from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import db_user
from app.db.database import get_db
from app.schemas.schemas import UserBase

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Create User
@router.post('/')
def create_user(request=UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read User

# Update User

# Delete User