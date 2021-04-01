from typing import Optional, List
from datetime import date, datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    joined: date


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class BaseUser(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name