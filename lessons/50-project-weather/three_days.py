# Practice 3: one answer. A three-day forecast with daily highs and lows
import requests

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_json(url, params):
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


city = get_json(GEO_URL, {"name": "Toronto", "count": 1})["results"][0]
params = {
    "latitude": city["latitude"],
    "longitude": city["longitude"],
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "auto",
    "forecast_days": 3,
}
daily = get_json(WEATHER_URL, params)["daily"]
print(f"{city['name']}, {city['country']}")
for day, high, low in zip(daily["time"], daily["temperature_2m_max"],
                          daily["temperature_2m_min"]):
    print(f"{day}: high {high} °C, low {low} °C")
