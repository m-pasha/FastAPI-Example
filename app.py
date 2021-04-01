from typing import Optional, List
from fastapi import FastAPI

# from models import Item

main = FastAPI()


def process_items(items: List[str]):
    for item in items:
        print(item)


@main.get("/")
async def root():
    return {"message": "Hello World 123"}


@main.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@main.put("/items/{item_id}")
def update_item(item_id: int, item: str):  # Item
    return {"item_name": item, "item_id": item_id}