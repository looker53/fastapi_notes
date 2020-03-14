"""body 参数声明。

body 参数有时候是一个嵌套的 json 类型。比如：
{
    "user": {
        "name": "yuz",
        "age": 6,
        "pwd": "123"
    },
    "type": 2,
    "level": 1
}


"""

import uvicorn
from enum import Enum
from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserModel(BaseModel):
    name: str
    pwd: str
    age: int

class UserType(Enum):
    NORMAL = 1
    ADMIN = 2
    STUFF = 3

class Level(Enum):
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    

class RegisterModel(BaseModel):
    user: UserModel
    type: UserType
    level: Level

@app.post("/user")
def home(body_data: RegisterModel):
    print(body_data.level)
    return {"msg": body_data}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)