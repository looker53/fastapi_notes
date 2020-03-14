"""Body Validation.

嵌套数据的列表表示。
hobby: List[HobbyModel]

如果要对 hobby 做限制呢？
hobby: List[HobbyModel] = Field(max_items=2)
TODO: 如何让多个 hobby 不重复呢？ 自定义 validator???

"""

import uvicorn
from typing import List
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class HobbyModel(BaseModel):
    name: str = Field(..., max_length=127)
    year: int = Field(0, le=100)
    level: int = 1


class UserInfo(BaseModel):
    """
    {
        "name": "wangzhen",
        "pwd": "123",
        "age": 11
    }
    """
    # alias 使用了以后，已经定义的 name 会失效
    name: str = Field(
        ..., alias='username', title='用户名', min_length=1,
        max_length=255
    )
    pwd: str = Field(..., min_length=6, max_length=255)
    age: int = Field(None, ge=16)
    hobby: List[HobbyModel] = Field(None, max_items=1)


class RegisterModel(BaseModel):
    """
    {
        "user_type": 1,
        "user_info": UserInfo
    }
    """
    user_type:int   # TODO: 使用 Enum 限制种类
    user_info:UserInfo


@app.post("/register")
def home(info: RegisterModel):
    return {"msg": info}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)