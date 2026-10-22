# Practice 2: catch both errors
try:
    lives = int(input("Lives: "))
    print("Damage per life:", 100 // lives)
except ValueError:
    print("Please type a whole number.")
except ZeroDivisionError:
    print("You need at least one life.")
