from typing import List
from pydantic import BaseModel, Field

class Genre(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description="Возраст автора должен быть указан в диапазоне от 15-90")

class Book(BaseModel):
    name: str
    title: str
    writer: str
    duration: str
    genre: List[Genre]
    peges: int