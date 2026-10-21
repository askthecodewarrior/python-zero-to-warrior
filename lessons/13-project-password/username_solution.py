# Password strength checker

# 1. Ask for the username and the password
username = input("Username: ")
password = input("Password: ")
length = len(password)
print(f"That's {length} characters")

# 2. Check it against common passwords
lowered = password.lower()
common = lowered == "password" or lowered == "password1!"

# 3. Give it a rating
if common:
    print("Weak: that's a common password")
elif lowered == username.lower():
    print("Weak: it's the same as your username")
elif length < 8:
    print("Weak: it's too short")
elif password.isdigit():
    print("OK: but it's only numbers")
elif length < 15:
    print("OK: but 15 or more characters is better")
else:
    print("Strong: 15 or more characters")
