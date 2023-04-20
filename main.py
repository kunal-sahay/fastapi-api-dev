from fastapi import FastAPI, status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    message: str
    data: str
    rating: Optional[int] = 2
    stream: str = "Stream Data"

my_posts = [
    {
        "message": "This is a test message 1",
        "data": "this is a test data 1",
        "id": 1
    },
    {
        "message": "This is a test message 2",
        "data": "this is a test data 2",
        "stream": "data stream",
        "id": 2
    }
]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"new_data": post}