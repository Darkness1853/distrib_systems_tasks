from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Заглушка для API
@app.get("/api/tasks")
def get_tasks():
    return {"tasks": []}