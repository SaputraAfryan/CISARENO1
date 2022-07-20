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
        "Status": data['status'],
        "results": data['results']
    }

@app.get("/bulan/{q}")
async def read_item(q: str):
    data = pnsController()
    data = data.show_by_month(q)
    return {
        "Status": data['status'],
        "results": data['results'],
        "q" : q
    }