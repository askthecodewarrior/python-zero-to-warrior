# One way to solve it: the weather in Fahrenheit and mph
import requests

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
SKY = {
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    51: "light drizzle",
    61: "slight rain",
    63: "moderate rain",
    95: "thunderstorm",
}


def get_json(url, params):
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def find_city(name):
    data = get_json(GEO_URL, {"name": name, "count": 1})
    results = data.get("results")
    if not results:
        return None
    return results[0]


def get_weather(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
    }
    return get_json(WEATHER_URL, params)["current"]


def report(name):
    city = find_city(name)
    if city is None:
        print(f"Can't find a city called {name}.")
        return
    now = get_weather(city["latitude"], city["longitude"])
    sky = SKY.get(now["weather_code"], "unknown")
    print(f"{city['name']}, {city['country']}: {sky}")
    print(f"Temperature: {now['temperature_2m']} °F")
    print(f"Wind: {now['wind_speed_10m']} mph")


def main():
    while True:
        name = input("City (or q to quit): ")
        if name == "q":
            break
        try:
            report(name)
        except requests.HTTPError as e:
            print("The weather service sent an error:", e)
        except requests.RequestException:
            print("Can't reach the weather service.")


if __name__ == "__main__":
    main()
