from typing import Optional, List
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# from models import Item


def get_application():
    main = FastAPI(title="Test", version="1.0.0")
    main.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return main


main = get_application()


def process_items(items: List[str]):
    for item in items:
        print(item)


@main.get("/")
async def root():
    return {"message": "Hello World!)"}


@main.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@main.put("/items/{item_id}")
def update_item(item_id: int, item: str):  # Item
    return {"item_name": item, "item_id": item_id}
