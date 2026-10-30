import json

text = json.dumps({"hp": 30, "alive": True, "pet": None})
print(text)
print(type(text))

data = json.loads(text)
print(data)
print(type(data))
