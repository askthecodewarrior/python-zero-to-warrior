# Lesson 50: Build a Weather App in Python with an API

Part of **Python: Zero to Warrior**, a free Python course for beginners. This project shows how to call an API in
Python with the requests package, and builds a small weather app with it.
Video: https://youtu.be/btyZN3OX-IY · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

Weather data by [Open-Meteo.com](https://open-meteo.com/), a free weather API. It's free for non-commercial use (like
learning) and needs no account and no API key. Keep your calls polite: the free tier allows fewer than 10,000 calls a
day. Your weather numbers are going to be different from the video's, because the API sends the weather right now.

## Before you start: install requests (lesson 48)
Make a virtual environment in your python-course folder, turn it on, and install requests into it:
```
python3 -m venv .venv               # Mac
source .venv/bin/activate
pip install requests

python -m venv .venv                # Windows
.venv\Scripts\activate
pip install requests
```
If you set the project up with uv, it's `uv add requests`. The prompt starts with `(.venv)` while the venv is on.

## What's in this lesson
- **An API is a website for programs.** Your program sends a request to a URL, and the website sends back data,
  usually as JSON, with a status code that says how it went (200 means it worked).
- **`first_call.py`: the raw call.**
  - `requests.get(url, params=params, timeout=10)` sends the request. `params` is a dictionary, and requests adds it to
    the end of the URL: `print(response.url)` shows `...search?name=Tokyo&count=1`. `timeout=10` stops waiting after
    10 seconds with no reply; without it, a request can wait forever.
  - `response.status_code` is `200`, and `response.json()` turns the JSON into Python dictionaries and lists.
  - `data["results"][0]` digs in: the `results` key holds a list, and `[0]` is the first match, another dictionary
    with `name`, `country`, `latitude` and `longitude`.
- **`weather.py`: the app.**
  - `GEO_URL` and `WEATHER_URL` are constants (capital letters), and `SKY` turns a few of the API's weather codes into
    words (the docs list 28; anything else shows `unknown`).
  - `get_json(url, params)` makes every call: `requests.get`, then `response.raise_for_status()`, which raises an
    `HTTPError` when the status is an error (like 400, a bad request), then `return response.json()`.
  - `find_city(name)` asks the geocoding API and uses `data.get("results")` (lesson 20): a name that isn't found comes
    back with no `results` key at all, so `.get()` gives `None` instead of a `KeyError`.
  - `get_weather(lat, lon)` asks the forecast API for `current` (`temperature_2m,wind_speed_10m,weather_code`, no
    spaces) and returns just the `current` dictionary.
  - `report(name)` prints the report, or `Can't find a city called ...`. The keys inside the f-strings use single
    quotes because the f-strings use double quotes.
  - `main()` asks for a city in a `while True` loop (lesson 16) until you type `q`. `except requests.HTTPError as e`
    comes first, and `except requests.RequestException` catches everything else requests raises, like no internet
    (`ConnectionError`) or a timeout (`Timeout`).
- **The common mistakes:**
  - A value the API doesn't know, like `"temperature_unit": "farenheit"`: the API answers 400, and its JSON says
    `Invalid value at 'temperature_unit'`. Spell it the way the docs do: `"fahrenheit"`.
  - Printing the response itself: `print(response)` prints `<Response [200]>`, the response object, not the data. Use
    `response.json()`.

## Files
- `first_call.py`, `weather.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs. `solution.py`: one way to solve it.
- `predict.py`, `feels_like.py`, `three_days.py`: practice problems 1, 2 and 3 (`feels_like.py` and `three_days.py`
  are one answer each: try them yourself first).

## Run it
```
python3 weather.py      # Mac
python weather.py       # Windows
```
Turn the venv on first. The same goes for every other file.

## Your turn
Show the weather in Fahrenheit and miles per hour: add `"temperature_unit": "fahrenheit"` and
`"wind_speed_unit": "mph"` to `get_weather()`'s params, then change `°C` to `°F` and `km/h` to `mph` in the prints.
`solution.py` does it; for Tokyo it printed a line like `Temperature: 62.4 °F` (yours will be different).

## Practice
1. Predict, then run `predict.py` (no internet needed: it uses part of a real reply from the video):
   ```python
   SKY = {0: "clear sky", 3: "overcast", 61: "slight rain"}
   now = reply["current"]
   print(now["temperature_2m"], reply["current_units"]["temperature_2m"])
   print(SKY.get(now["weather_code"], "unknown"))
   print(SKY.get(45, "unknown"))
   print(now.get("rain"))
   ```
   (`7.2 °C`, `clear sky`, `unknown` and `None`: 45 isn't in this small `SKY`, and the reply has no `rain` key.)
2. Write `feels_like.py`: ask the forecast API for `apparent_temperature` as well (the "feels like" temperature) and
   print both, like `Cairo: 26.2 °C` and `Feels like: 25.7 °C`.
3. Write `three_days.py`: ask for `"daily": "temperature_2m_max,temperature_2m_min"` with `"timezone": "auto"` and
   `"forecast_days": 3` (the API needs a timezone for daily values), then loop over the days with `zip()` (lesson 21)
   and print each one, like `2026-10-31: high 14.7 °C, low 4.9 °C`.

More ideas: let the user type `f` to switch between Celsius and Fahrenheit, or show the time the reading is from
(`now["time"]`).
