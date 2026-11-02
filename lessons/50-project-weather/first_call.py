# My first API call
import requests

url = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name": "Tokyo", "count": 1}
response = requests.get(url, params=params, timeout=10)
print(response.status_code)
print(response.url)

data = response.json()
city = data["results"][0]
print(city["name"], city["country"])
print(city["latitude"], city["longitude"])
