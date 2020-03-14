"""请求参数默认值和可选值"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home(page:int=1, user=None):
    if not user:
        return {"msg": f"welcome to {page}, 陌生人"}
    return {"msg": f"welcome to {page}, {user}"}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)