from sqlalchemy.orm import Session
from app.db.hash import Hash
from app.db.models import DbUser
from app.schemas.schemas import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user