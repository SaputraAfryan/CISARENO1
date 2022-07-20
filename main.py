# main.py

from typing import Union

from fastapi import FastAPI
from controllers.pnsController import pnsController

app = FastAPI()

@app.get("/")
async def root():
    data =  pnsController()
    data = data.show_all()
    return {
        "Status": data.status,
        "results": data.results
    }

@app.get("/{item_id}")
async def read_item(q: Union[str, None] = None):
    data =  pnsController()
    return data.show_by_month(q)