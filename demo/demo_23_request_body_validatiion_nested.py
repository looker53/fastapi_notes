"""Body Validation.

1, 通过 BaseModel;
2, 通过 Body;

这个例子使用 BaseModel.

BaseModel 分为 2 种：
- 1， 使用 key
- 2,  不使用 key. 

限制每个field 的数据类型和长度。 Field

1， 在 Field 中，alias 使用了以后，已经定义的 name 会失效


嵌套数据。

通过 BaseModel 验证数据：
1，user_type:int 为必须参数，不传会报错
2，通过 Field 验证时，第一个参数为默认值，如果需要是必传参数，用 ... 表示。

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