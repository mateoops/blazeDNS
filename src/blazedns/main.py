from fastapi import FastAPI

from .routers import sites

app = FastAPI()

app.include_router(sites.router)