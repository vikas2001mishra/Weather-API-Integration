from typing import List
from coord import Coord
from weather import Weather
from main_data import MainData
from wind import Wind
from clouds import Clouds
from sys_info import Sys

class WeatherData:
    def __init__(self, coord: Coord, weather: List[Weather], base: str, main: MainData, visibility: int, wind: Wind, clouds: Clouds, dt: int, sys: Sys, timezone: int, id: int, name: str, cod: int):
        self.coord = coord
        self.weather = weather
        self.base = base
        self.main = main
        self.visibility = visibility
        self.wind = wind
        self.clouds = clouds
        self.dt = dt
        self.sys = sys
        self.timezone = timezone
        self.id = id
        self.name = name
        self.cod = cod
