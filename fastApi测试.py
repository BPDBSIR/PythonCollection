from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexent",
    renet = "renet",
    lenet = "lenet"


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


@app.get("/")
async def root():
    return Person("Andrew", 20)


@app.get("/index")
async def index():
    return "index"


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/login")
async def login(username: str, password: str):
    return {
        "username": username,
        "password": password
    }
