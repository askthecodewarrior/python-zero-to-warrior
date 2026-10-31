# Your turn: give Bank a total() method
from account import Account


class SavingsAccount(Account):
    def __init__(self, owner, rate):
        super().__init__(owner)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate // 100
        if interest > 0:
            self.deposit(interest)


class Bank:
    def __init__(self):
        self.accounts = {}

    def add(self, account):
        self.accounts[account.owner] = account

    def transfer(self, sender, receiver, cents):
        self.accounts[sender].withdraw(cents)
        self.accounts[receiver].deposit(cents)

    # TODO: def total(self): add up every account's balance and return it


ava = Account("Ava")
ben = SavingsAccount("Ben", 2)
bank = Bank()
bank.add(ava)
bank.add(ben)
ava.deposit(5000)
bank.transfer("Ava", "Ben", 2000)
ben.add_interest()
print(ava)
print(ben)
# TODO: print the total in dollars, like Total: $50.40
