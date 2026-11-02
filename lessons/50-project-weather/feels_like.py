# Practice 2: one answer. Ask for the "feels like" temperature too
import requests

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_json(url, params):
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


city = get_json(GEO_URL, {"name": "Cairo", "count": 1})["results"][0]
params = {
    "latitude": city["latitude"],
    "longitude": city["longitude"],
    "current": "temperature_2m,apparent_temperature",
}
now = get_json(WEATHER_URL, params)["current"]
print(f"{city['name']}: {now['temperature_2m']} °C")
print(f"Feels like: {now['apparent_temperature']} °C")
