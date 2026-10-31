# A bank account that guards its own money
from dataclasses import dataclass


@dataclass
class Transaction:
    kind: str
    cents: int


class Account:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0  # in cents
        self.history = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, cents):
        if cents <= 0:
            raise ValueError("amount must be positive")
        self._balance += cents
        self.history.append(Transaction("deposit", cents))

    def withdraw(self, cents):
        if cents <= 0:
            raise ValueError("amount must be positive")
        if cents > self._balance:
            raise ValueError("not enough money")
        self._balance -= cents
        self.history.append(Transaction("withdraw", cents))

    def __str__(self):
        return f"{self.owner}: ${self._balance / 100:.2f}"


if __name__ == "__main__":
    zoe = Account("Zoe")
    zoe.deposit(5000)
    zoe.withdraw(1250)
    print(zoe)
    for item in zoe.history:
        print(item)
