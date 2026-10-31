# Practice 2: a CheckingAccount charges a fee on every withdrawal
from account import Account


class CheckingAccount(Account):
    def __init__(self, owner, fee):
        super().__init__(owner)
        self.fee = fee

    def withdraw(self, cents):
        if cents <= 0:
            raise ValueError("amount must be positive")
        super().withdraw(cents + self.fee)


sam = CheckingAccount("Sam", 150)
sam.deposit(10000)
sam.withdraw(2000)
print(sam)
try:
    sam.withdraw(7900)
except ValueError as e:
    print("Error:", e)
print(sam)
