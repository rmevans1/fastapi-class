from fastapi import FastAPI
from .routers import blog_get

app = FastAPI()
app.include_router(blog_get.router) #import router

@app.get('/hello')
def index():
    return {'message': 'Hello World!'}


