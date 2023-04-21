from sqlalchemy.orm import Session
from app.db.models import DbArticle
from app.schemas.schemas import ArticleBase

def create_article(db: Session, request: ArticleBase):
    pass

def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    # Handle Errors
    return article