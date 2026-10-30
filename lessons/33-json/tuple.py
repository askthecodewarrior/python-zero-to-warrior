# Practice 1: what comes back?
import json

spot = {"x": 3, "pos": (3, 4), "alive": False}
text = json.dumps(spot)
print(text)

back = json.loads(text)
print(back)
print(type(back["pos"]))
