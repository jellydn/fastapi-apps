import os
import time

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .routers import items, users

# Define the FastAPI app
app = FastAPI()

# -------------------
# Middleware Setup
# -------------------

# Add CORS middleware to allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# -------------------
# Model Definitions
# -------------------


class HelloMessage(BaseModel):
    Hello: str


# -------------------
# Route Definitions
# -------------------


@app.get("/", response_model=HelloMessage, tags=["root"])
def read_root():
    """Return a simple hello world message"""
    return {"Hello": "World"}


app.include_router(items.router)
app.include_router(users.router)


# -------------------
# Main execution for debugging
# -------------------
if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)
