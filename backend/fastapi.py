from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/form")
def readministry():
    return [
      { name: "กระทรวง1", key: "1" },
      { name: "กระทรวง2", key: "2" }
    ]