from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/min")
def read_root():
    return [{"name": 'กระทรวง1', "key": '1'}, {"name": 'กระทรวง2', "key": '2'}]