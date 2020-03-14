"""返回流,分片段返回"""


import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

async def get_file():
    with open("demo.mp4", "rb") as f:
        while True:
            chuck = f.read(5000)
            if not chuck:
                break
            yield chuck

@app.get('/file')
def file():
    return StreamingResponse(get_file(), media_type='video/mp4')

if __name__ == "__main__":
    uvicorn.run(app)