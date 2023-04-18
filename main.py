from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def index():
    return {'message': 'Hello World!'}

@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f'Blog with id {id}'}
