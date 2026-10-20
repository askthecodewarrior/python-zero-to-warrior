# Health bar status
health = int(input("Health: "))

if health >= 70:
    print("Strong")
elif health >= 30:
    print("Hurt")
else:
    print("Danger!")
