"""query string 校验。

注意：这种只能校验 query string. 不能校验url路径 /user/{id}
"""

import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()

@app.post("/user")
def home(id:int=Query(None, ge=9)):
    return {"msg": id}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)