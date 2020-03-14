import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/other/{path_file:path}")
def other(path_file: str):
    return {"msg": path_file}


if __name__ == "__main__":
    uvicorn.run(app)