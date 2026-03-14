from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
import uvicorn
import uuid

orders= []

@strawberry.type
class Order:
    id: str
    name: str
    price: float
    status: str
    priority: int

@strawberry.type
class Query:
    @strawberry.field
    def orders(self) -> List[Order]:
        return orders
    
    @strawberry.field
    def order(self, id: str) -> Optional[Order]:
        for order in orders:
            if order.id == id:
                return order
        return None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_order(self, name: str, price: float, status: str, priority: int) -> Order:
        new_order = Order(
            id=str(len(orders)+1),
            name=name,
            price=price,
            status=status,
            priority=priority
        )
        orders.append(new_order)
        return new_order

schema = strawberry.Schema(query=Query, mutation=Mutation)
app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8222)