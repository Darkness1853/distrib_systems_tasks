from fastapi import FastAPI

app = FastAPI(title="Other")

@app.get("/api/other/")
def get_other():
    return {"message": "Это другой сервис"}