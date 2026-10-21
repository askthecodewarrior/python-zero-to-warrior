# Practice 2: count the tries in gate.py
password = ""
tries = 0
while password != "dragon":
    password = input("Password: ")
    tries += 1

print(f"The gate opens after {tries} tries!")

# Practice 3: keep asking until the door number is 1, 2 or 3
door = 0
while door < 1 or door > 3:
    door = int(input("Pick a door (1-3): "))

print("You open door", door)
