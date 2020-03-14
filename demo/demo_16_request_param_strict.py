"""数据类型严格模式。

实际上， user:int = None 这种写法是不严谨的。
明明已经声明类型是 int 了， 怎么可能有个默认值是 None 呢？
"""

import uvicorn
from typing import Union, Optional
from fastapi import FastAPI

app = FastAPI()

@app.post("/user")
def home(user: Optional[int, bool, list]=None):
    return {"msg": user}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)