from fastapi import FastAPI
from app.routers import blog_get, blog_post
from app.db import models
from app.db.database import engine

app = FastAPI()
app.include_router(blog_get.router) #import router
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message': 'Hello World!'}

models.Base.metadata.create_all(engine)

