"""自动参数校验"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

# http://localhost:8000?name=yuz
@app.get("/")
def home(name:str='yuz'):
    return {"msg": name}

# http://localhost:8000/users/23
# 只能是数字，如果是 abc 这样的字母，会报错。
@app.get("/users/{id}")
def user(id: int):
    return {"msg": f"welcome login, {id}"}


if __name__ == "__main__":
    uvicorn.run(app, debug=True)