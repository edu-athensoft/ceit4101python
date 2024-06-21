# main.py
from weather import get_weather, parse_weather_data
from mycalendar import get_date, get_datetime


def main():
    print("Welcome to the Weather Query Utility!")
    print("ver 1.0.0")
    city_name = input("Enter the city name: ")

    # display datetime info
    print(f"\nDate of Today: {get_datetime()}")

    # display weather info
    weather_data = get_weather(city_name)
    weather_info = parse_weather_data(weather_data)

    print(f"\nWeather information for {city_name}:\n{weather_info}")


if __name__ == "__main__":
    main()
