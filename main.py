from typing import Optional
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel


class ModelName(str, Enum):
    bert = "bert"
    gpt = "gpt"
    electra = "electra"

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}") # 선언된 순서대로 생긴다.
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/models/{model_name}")
async def get_model_fangtion(model_name: ModelName):
    """
        문서도 자동으로 올라가나?
        + 마크다운인가?
        `markdown`?
    """
    if model_name == ModelName.bert:
        return {"model_name": ModelName.bert}
    if model_name == ModelName.electra:
        return {"model_name": ModelName.electra}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path", file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip+limit]