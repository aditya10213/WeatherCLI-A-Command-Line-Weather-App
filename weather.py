import sys
import requests

from utils import format_weather

API_URL = "https://api.open-meteo.com/v1/forecast"

def get_weather(city):
    params = {
        "latitude": 28.7041 if city == "delhi" else 19.0760,
        "longitude": 77.1025 if city == "delhi" else 72.8777,
        "current_weather": True
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    return data["current_weather"]

def main():
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
        return

    city = sys.argv[1].lower()
    weather = get_weather(city)
    print(format_weather(city, weather))

main()
if len(sys.argv) < 2:
    print("City name missing. Example:")
    print("python weather.py delhi")
    return

