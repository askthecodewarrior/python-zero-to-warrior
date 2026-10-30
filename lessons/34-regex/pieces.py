import re

msg = "Hit 3 orcs for 25 gold"
print(re.findall(r"\d", msg))
print(re.findall(r"[aeiou]", msg))
print(re.findall(r"g..d", msg))
