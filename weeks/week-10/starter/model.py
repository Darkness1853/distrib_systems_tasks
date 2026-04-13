from pydantic import BaseModel

class Review(BaseModel):
    id: int
    rating: int
    text: str