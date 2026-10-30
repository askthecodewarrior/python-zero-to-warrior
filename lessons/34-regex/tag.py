# Check a player tag: letters, digits and _ only
import re

tag = input("Player tag: ")
if re.search(r"^\w+$", tag):
    print("Good tag")
else:
    print("Letters, digits and _ only")
