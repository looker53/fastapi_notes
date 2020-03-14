"""Body Validation.

embed 形式：
>>> def home(user: UserInfo = Body(..., embed=True)):

则所传的参数必须带 user 的 key:
{
    "user": {
        "name": "wangzhen",
        "pwd": "123",
        "age": 11
    }
}

这样会报错：
{
    "name": "wangzhen",
    "pwd": "123",
    "age": 11
}

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
def home(user: UserInfo = Body(..., embed=True)):
    return {"user": user}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)