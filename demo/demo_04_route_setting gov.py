"""路由。
集中注册
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


def home():
    return {"msg": "hello world"}
app.add_api_route("/", home, methods=["get", "post"])

if __name__ == "__main__":
    uvicorn.run(app, debug=True)