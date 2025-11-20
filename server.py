from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/api/data")
async def get_data():
    return {"message": "Hello from FastAPI backend!"}

# Serverless adapter
handler = Mangum(app)
