from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    location: int


class ItemResponse(Item):
    id: int


# Model for resonse_model in main to return data in correct order
class ItemResponseTemplate(BaseModel):
    id: int
    name: str
    description: str
    location: int


class Location(BaseModel):
    id: int
    name: str
    process: str
    address: str
