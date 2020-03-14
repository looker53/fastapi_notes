"""枚举类型校验。

为什么要使用枚举类型呢？可读性会更高。

"""

import uvicorn
from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class UserType(Enum):
    STUDENT:str = 1
    TEACHER:str = 2
    WORKER:str = 3


@app.get("/users")
def user(type: UserType):
    if type == UserType.TEACHER:
        return {"msg": type}
    elif type.value == 1:
        return {"msg": "hello, student"}
    return {"msg": "hello, others"}


if __name__ == "__main__":
    uvicorn.run(app, debug=True)