from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
import uvicorn

photos = []

@strawberry.type
class Photo:
    id: str
    title: str
    url: str

@strawberry.type
class Query:
    @strawberry.field
    def photos(self) -> List[Photo]:
        return photos
    
    @strawberry.field
    def photo(self, id: str) -> Optional[Photo]:
        for photo in photos:
            if photo.id == id:
                return photo
        return None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_photo(self, title: str, url: str) -> Photo:
        new_photo = Photo(
            id=str(len(photos) + 1),
            title=title,
            url=url
        )
        photos.append(new_photo)
        return new_photo

schema = strawberry.Schema(query=Query, mutation=Mutation)
app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8135)