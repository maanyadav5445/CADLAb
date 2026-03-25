class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def transfer(self, other, amount):
        if amount <= self.balance:
            self.balance -= amount
            other.balance += amount

accounts = {}

while True:
    choice = input()
    if choice == "1":
        name = input()
        balance = int(input())
        accounts[name] = Account(name, balance)
    elif choice == "2":
        name = input()
        amount = int(input())
        accounts[name].deposit(amount)
    elif choice == "3":
        name = input()
        amount = int(input())
        accounts[name].withdraw(amount)
    elif choice == "4":
        a = input()
        b = input()
        amount = int(input())
        accounts[a].transfer(accounts[b], amount)
    elif choice == "5":
        for acc in accounts.values():
            print(acc.name, acc.balance)
    elif choice == "6":
        break