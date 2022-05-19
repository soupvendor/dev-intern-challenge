from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    location: int


class ItemResponse(Item):
    id: int


class Location(BaseModel):
    id: int
    name: str
    process: str
    address: str
