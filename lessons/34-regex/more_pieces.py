import re

msg = "Hit 3 orcs for 25 gold"
print(re.findall(r"\d+", msg))
print(re.findall(r"orcs?", "1 orc and 3 orcs"))
print(re.search(r"^\d+$", "2026"))
print(re.search(r"^\d+$", "20x6"))
