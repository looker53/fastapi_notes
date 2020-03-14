"""路由。

一个函数可以定义多个路由吗？
一个函数可以定义多种请求方法吗？
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.post("/")
@app.get("/hello")
def home():
    return {"msg": "hello world"}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)