"""
Module for custom exceptions for all services related to weather.
"""


class WeatherServiceNotAvailableException(Exception):
    """Exception raised if external service is not available."""

    def __init__(self, status_code: int, detail: str) -> None:
        super().__init__()
        self.status_code = status_code
        self.detail = detail
