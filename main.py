from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.pns import pns
from routes.apbd import apbd
from routes.apbn import apbn

app = FastAPI()

def cors_headers(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
        )
    return app

app.include_router(pns)
app.include_router(apbn)
app.include_router(apbd)

@app.get("/")
async def root():
    return {"message": "Check server documentation"}