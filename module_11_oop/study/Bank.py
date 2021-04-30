"""
OOP
Business Entity: BankAccount
"""


class BankAccount:

    # constructor
    def __init__(self, accountId, accountName, balance):
        self.accountId = accountId
        self.accountName = accountName
        self.balance = balance

    # method
    def deposit(self, amount):
        self.balance += amount

    # method
    def withdraw(self, amount):
        self.balance -= amount

    # comparison method
    def __lt__(self, other):
        return self.balance < other.balance

    # comparison method
    def __gt__(self, other):
        return self.balance > other.balance

    # tostring
    def __str__(self):
        return "("+self.accountId+","+self.accountName+","+str(self.balance)+")"
