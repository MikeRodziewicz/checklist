"""
Endpoints to fetch weather and general conditions data.
"""

from fastapi import APIRouter, Depends, HTTPException

from main.exceptions.weather_exceptions import WeatherServiceNotAvailableException
from main.services.weather_service import WeatherService, get_weather_service 

weather_router = APIRouter()


@weather_router.get("/weather")
def weather_get(weather_service: WeatherService = Depends(get_weather_service)):
    """Return weather description"""

    try:
        print("here entering into the endoint")
        weather = weather_service.provide_weather() 
    except WeatherServiceNotAvailableException as err:
        raise HTTPException(status_code=424, detail=err)
    except:
        raise HTTPException(status_code=500, detail="Something went wrong...")
    return {'weather': weather}

