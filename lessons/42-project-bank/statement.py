# Practice 3: a statement with + for deposits and - for withdrawals
from account import Account


def statement(account):
    for item in account.history:
        if item.kind == "deposit":
            sign = "+"
        else:
            sign = "-"
        print(f"{sign}${item.cents / 100:.2f}")
    print(account)


lee = Account("Lee")
lee.deposit(4000)
lee.withdraw(1575)
lee.deposit(250)
statement(lee)
