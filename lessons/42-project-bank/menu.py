# Bonus: a text menu for one account (lessons 14, 27 and this one)
from account import Account

account = Account("You")
while True:
    print(account)
    choice = input("d = deposit, w = withdraw, h = history, q = quit: ")
    if choice == "q":
        break
    if choice == "h":
        for item in account.history:
            print(item)
        continue
    if choice not in ("d", "w"):
        print("Please type d, w, h or q.")
        continue
    try:
        cents = int(input("Amount in cents: "))
        if choice == "d":
            account.deposit(cents)
        else:
            account.withdraw(cents)
    except ValueError as e:
        print("Sorry:", e)
print("Goodbye!")
