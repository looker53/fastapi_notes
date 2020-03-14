"""数据可能是多种类型， Union"""

import uvicorn
from typing import Union, Optional
from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def home(user: Union[int, bool, list]=None):
    return {"msg": user}

@app.post("/user")
def home(user: Optional[int, bool, list]=None):
    return {"msg": user}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)