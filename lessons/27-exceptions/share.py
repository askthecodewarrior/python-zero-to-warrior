# Share the gold between the players
try:
    gold = int(input("Gold: "))
    players = int(input("Players: "))
    share = gold // players
except ValueError:
    print("Please type whole numbers.")
except ZeroDivisionError:
    print("You need at least one player.")
else:
    print("Each player gets", share)
finally:
    print("Done sharing.")
