import re

loot = "Level 7, 250 gold, 3 keys"
print(re.findall(r"\d", loot))
print(re.findall(r"\d+", loot))
print(re.sub(r"\d+", "#", loot))
