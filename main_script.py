import json
from weather_data import WeatherData
from coord import Coord
from weather import Weather
from main_data import MainData
from wind import Wind
from clouds import Clouds
from sys_info import Sys

def map_json_to_weather_data(json_data):
    coord = Coord(**json_data['coord'])
    weather = [Weather(**w) for w in json_data['weather']]
    main = MainData(**json_data['main'])
    wind = Wind(**json_data['wind'])
    clouds = Clouds(**json_data['clouds'])
    sys = Sys(**json_data['sys'])
    weather_data = WeatherData(
        coord, weather, json_data['base'], main, json_data['visibility'],
        wind, clouds, json_data['dt'], sys, json_data['timezone'],
        json_data['id'], json_data['name'], json_data['cod']
    )
    return weather_data

# Load JSON data from a file
with open('../../jsonparsing.py/pythonProject1/.venv/WeatherData.json', 'r') as json_file:
    json_data = json.load(json_file)
# Map JSON data to WeatherData object
weather_data = map_json_to_weather_data(json_data)

# Convert temperature from Kelvin to Celsius
temperature_celsius = weather_data.main.temp - 273.15

# Accessing data
print(f"City: {weather_data.name}")
print(f"Country: {weather_data.sys.country}")
print(f"Wind Speed: {weather_data.wind.speed} m/s")
print(f"Temperature: {temperature_celsius:.2f}°C")
print(f"Weather: {weather_data.weather[0].main}")
print(f"Description: {weather_data.weather[0].description}")
print(f"Coordinates: ({weather_data.coord.lon}, {weather_data.coord.lat})")
