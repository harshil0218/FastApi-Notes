from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.5',port=9000)

class Blog(BaseModel):
    title : str
    body: str
    published: Optional[bool]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/blog")

def index(limit:int = 5,published:bool=True , sort:Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from list"}
    
    return {"data": f"{limit} unpublished blogs from list"}

# fast api reads line by line so we nedd to arramge the order of the functions
# if any function accepting dynamic parameter then it should be at the end

@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog is created with title as {blog.title}"}

@app.get('blog/unpublished')
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}

@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {"1", "2"}}



