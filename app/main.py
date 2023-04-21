from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions import StoryException
from app.routers import blog_get, blog_post, user, article
from app.db import models
from app.db.database import engine

app = FastAPI()
app.include_router(article.router)
app.include_router(user.router)
app.include_router(blog_get.router) #import router
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message': 'Hello World!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )

models.Base.metadata.create_all(engine)

