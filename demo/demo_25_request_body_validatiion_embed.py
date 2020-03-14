"""Body Validation.
在视图函数中定义多个参数。

定义 body 参数的 3 种方式：
1， 统一用一个 ItemModel 
>>> def home(info: RegisterModel):
2, 分成多个 Model
>>> def home(user: UserModel, other: OtherModel):
3, 单个参数用 Body()
>>> def home(user: UserModel, user_type: Body(...)):

"""

import uvicorn
from typing import List
from fastapi import FastAPI, Query, Body
from pydantic import BaseModel, Field

app = FastAPI()


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



@app.post("/register")
def home(user: UserInfo, user_type:int = Body(1,ge=1, le=5)):
    return {"user": user, "user_type": user_type}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)