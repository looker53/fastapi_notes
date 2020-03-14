"""body 参数声明。

body 参数校验需要配合 pydantic 使用。

如何自定义错误返回数据？请详细阅读 pydantic 的官方文档。
"""

import uvicorn
from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserData(BaseModel):
    name: str
    pwd: str
    age: int

@app.post("/user")
def home(user: UserData):
    return {"msg": user}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)