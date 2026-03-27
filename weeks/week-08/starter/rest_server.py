from fastapi import FastAPI
import uvicorn

app = FastAPI()
orders_db = {}

@app.get("/api/orders")
def get_orders():
    return list(orders_db.values())

@app.post("/api/orders")
def create_order(id: str, priority: int):
    order = {"id": id, "priority": priority}
    orders_db[id] = order
    return order

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8122)