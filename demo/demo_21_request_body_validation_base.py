"""Body Validation.

1, 通过 BaseModel;
2, 通过 Body;

这个例子使用 BaseModel.

BaseModel 分为 2 种：
- 1， 使用 key
- 2,  不使用 key. 
"""

import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class UserInfo(BaseModel):
    """
    {
        "name": "wangzhen",
        "pwd": "123",
        "age": 11
    }
    """
    name: str
    pwd: str
    age: int


@app.post("/register")
def home(info: UserInfo):
    return {"msg": info}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)