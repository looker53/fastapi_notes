"""返回流"""


import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get('/file')
def file():
    file = open("demo.mp4", 'rb')
    return StreamingResponse(file, media_type='video/mp4')

if __name__ == "__main__":
    uvicorn.run(app)