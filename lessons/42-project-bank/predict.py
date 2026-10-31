# Practice 1: predict, then run
from account import Account

kim = Account("Kim")
kim.deposit(2000)
try:
    kim.deposit(0)
except ValueError as e:
    print("Error:", e)
try:
    kim.withdraw(-500)
except ValueError as e:
    print("Error:", e)
print(kim)
print(len(kim.history))
