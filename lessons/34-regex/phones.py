# Find phone numbers in a message
import re

text = "Call 555-1234 or 555-9876 after 6 PM"
match = re.search(r"\d+-\d+", text)
print(match)
print(match.group())

numbers = re.findall(r"\d+-\d+", text)
print(numbers)

safe = re.sub(r"\d+-\d+", "XXX-XXXX", text)
print(safe)
