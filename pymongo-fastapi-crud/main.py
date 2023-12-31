from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from contextlib import asynccontextmanager

config = dotenv_values(".env")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start db client
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
    yield

    app.mongodb_client.close()

    # Release resources, shut down db client


USE_LIFESPAN = True

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}
