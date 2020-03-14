"""query string 校验。
Query 对象
注意：这种只能校验 query string. 不能校验url路径 /user/{id}

Path 对象：
校验路径
"""

import uvicorn
from fastapi import FastAPI, Query
from pydantic import Field

app = FastAPI()

@app.get("/user")
def home(id:int=Query(None, ge=9)):
    return {"msg": id}


# Query 对象能否提出？ 可以，不过放到路由这里更加方便管理。
# 1,单独提取出来会增加复杂度。

# 对于太长的校验会非常影响可读性
# 2, 统一放到 validate 模块当中。
q = Query(None, min_length=6, max_length=255)

@app.get("/user-info")
def user_info(id:str = q):
    return {"msg": id}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)