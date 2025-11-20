from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from any origin (React frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend URL
    allow_methods=["*"],
    allow_headers=["*"]
)

# Simple GET endpoint
@app.get("/api/data")
async def get_data():
    return {"message": "Hello from FastAPI backend!"}
