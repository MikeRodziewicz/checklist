"""
Initialize app and provide FastAPI object.
"""
from fastapi import APIRouter, Depends, FastAPI

from main.routes.weather import weather_router

app = FastAPI() 
root_router = APIRouter(tags=["root"])



@root_router.get("/")
def root_get():
    return {'Response': 'OK'}


app.include_router(root_router)
app.include_router(weather_router)
