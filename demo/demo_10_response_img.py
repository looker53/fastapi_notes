import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get('/file')
def file():
    return FileResponse('yy.png')

if __name__ == "__main__":
    uvicorn.run(app)