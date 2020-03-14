"""Body Validation.

1, 通过 BaseModel;
2, 通过 Body;

这个例子使用 BaseModel.

BaseModel 分为 2 种：
- 1， 使用 key
- 2,  不使用 key. 

限制每个field 的数据类型和长度。 Field

1， 在 Field 中，alias 使用了以后，已经定义的 name 会失效
"""

import uvicorn
from fastapi import FastAPI, Query
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
def home(info: UserInfo):
    return {"msg": info}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)