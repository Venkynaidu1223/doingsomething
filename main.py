
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def health():
    return {"message": "API is running"}

@app.post("/items")
def create_item(item: Item):
    return {"item": item}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
