"""
[Homework]
Date: 2022-03-27
Due date: 2022-04-02
1. Programming practice
Rewrite the program (Bank Interest Rate) applying polymorphism
"""

# entity layer
class Bank:
    def __init__(self, interestRate):
        self.interestRate = interestRate

    def getInterestRate(self):
        return self.interestRate


class BankA(Bank):
    def getInterestRate(self):
        return self.interestRate


class BankB(Bank):
    def getInterestRate(self):
        return self.interestRate


class BankC(Bank):
    def getInterestRate(self):
        return self.interestRate


class BankD(Bank):
    def getInterestRate(self):
        return self.interestRate


# service layer
class BankUtil:
    def queryInterestRate(self, bankObj):
        result = bankObj.getInterestRate()
        return result


"""
design a function to
receive bank id or name
generate bankObject

"""
# main

def generateBankObj(bankName):
    bankObj = None
    if bankName=='A':
        bankObj = BankA(0.04)
    if bankName=='B':
        bankObj = BankB(0.0395)
    if bankName=='C':
        bankObj = BankC(0.035)
    if bankName== 'D':
        bankObj = BankD(0.05)
    return bankObj

# application layer

myapp = BankUtil()

print("welcome to bank checking system")
print("Here are three banks to choose from:")
print("Choose BankA, press A.")
print("Choose BankB, press B.")
print("Choose BankC, press C.")
print("Choose BankC, press D.")

var = str(input("Please choose the bank that you want to check :"))

bankObj = generateBankObj(var)
result = myapp.queryInterestRate(bankObj)
print(f'The interest rate of this bank is {result:.3%}')


