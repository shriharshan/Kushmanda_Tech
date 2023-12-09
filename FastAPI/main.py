from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
import os
from api.api import router as get_net_image_prediction
from database.database import init_db

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers    
 )

app.include_router(get_net_image_prediction)

if __name__ == "__main__":
    init_db() 
