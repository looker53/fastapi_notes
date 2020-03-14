"""路由的顺序需要注意。


"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

# 这个固定参数的路由应该放在通用匹配的路由前面。
# 如果放在通用路由后面，会不生效。
@app.get("/users/my")
def user_me():
    return {"msg": "hello, this is your user page"}

@app.get("/users/{name}")
def user(name: str):
    return {"msg": f"welcome login, {name}"}




if __name__ == "__main__":
    uvicorn.run(app, debug=True)