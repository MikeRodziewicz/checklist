"""
Module for checking the weather conditions using external service.
"""
from collections.abc import Generator

class WeatherClient(Client):
    pass

class WeatherService:

    def provide_weather(self) -> str:
        print("here entering into the service")
        return "Cold"

def get_weather_service() -> Generator[WeatherService, None, None]:
    print("here entering into the generator")
    weather_service = WeatherService()
    yield weather_service 
