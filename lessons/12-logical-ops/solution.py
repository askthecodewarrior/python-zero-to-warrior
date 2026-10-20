# Can the player open the door?
has_key = True
level = 3
stunned = False

print(has_key and level >= 5)
print(has_key or level >= 5)
print(not stunned)

if has_key and level >= 5:
    print("The door opens.")
else:
    print("The door is locked.")

print(True or False and False)
print((True or False) and False)
