# weather.py
import requests
from utils import get_api_key


def get_weather(city_name):
    """
    Fetches the current weather for the given city name using OpenWeatherMap API.
    """
    api_key = get_api_key()
    if not api_key:
        return None

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data for {city_name}. HTTP Status Code: {response.status_code}")
        return None


def parse_weather_data(data):
    """
    Parses the weather data and returns a formatted string.
    """
    if data:
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        description = weather['description']
        temperature = main['temp']
        humidity = main['humidity']
        wind_speed = wind['speed']

        weather_info = (
            f"Weather: {description}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        return weather_info
    else:
        return "No weather data available."