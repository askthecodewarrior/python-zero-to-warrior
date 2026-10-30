# Practice 2: settings that stay switched (one answer)
import json

try:
    with open("settings.json") as f:
        settings = json.load(f)
except FileNotFoundError:
    settings = {"sound": True, "volume": 7}

settings["sound"] = not settings["sound"]
if settings["sound"]:
    print("Sound: on")
else:
    print("Sound: off")

with open("settings.json", "w") as f:
    json.dump(settings, f, indent=2)
