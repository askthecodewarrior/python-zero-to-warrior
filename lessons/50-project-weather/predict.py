# Practice 1: predict what this prints, then run it (no internet needed)
# "reply" is part of the real reply the API sent for Paris in the video
SKY = {0: "clear sky", 3: "overcast", 61: "slight rain"}
reply = {
    "current_units": {"temperature_2m": "°C", "wind_speed_10m": "km/h"},
    "current": {
        "temperature_2m": 7.2,
        "wind_speed_10m": 5.4,
        "weather_code": 0,
    },
}
now = reply["current"]
print(now["temperature_2m"], reply["current_units"]["temperature_2m"])
print(SKY.get(now["weather_code"], "unknown"))
print(SKY.get(45, "unknown"))
print(now.get("rain"))
