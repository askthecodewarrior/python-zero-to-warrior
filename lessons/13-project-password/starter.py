# Lesson 13, your turn: check the username too
# Fill in each TODO, save the file, then run it:
#   Mac:     python3 starter.py
#   Windows: python starter.py
# Type pixel_knight for both. You should see:
#   Weak: it's the same as your username

# 1. Ask for the username and the password
# TODO 1: ask for the username, before the password
password = input("Password: ")
length = len(password)
print(f"That's {length} characters")

# 2. Check it against common passwords
lowered = password.lower()
common = lowered == "password" or lowered == "password1!"

# 3. Give it a rating
if common:
    print("Weak: that's a common password")
# TODO 2: add an elif: when lowered matches the username in lowercase,
#         print "Weak: it's the same as your username"
elif length < 8:
    print("Weak: it's too short")
elif password.isdigit():
    print("OK: but it's only numbers")
elif length < 15:
    print("OK: but 15 or more characters is better")
else:
    print("Strong: 15 or more characters")
