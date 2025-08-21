from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()


@app.get("/ping")
async def pong():
    return Response("pong", media_type="text/plain", status_code=200)
