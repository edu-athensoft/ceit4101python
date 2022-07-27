"""
[Homework]
Date: 2022-03-27
Due date: 2022-04-02
1. Programming practice
Rewrite the program (Bank Interest Rate) applying polymorphism

for-loop and collection

"""

# entity layer
class Bank:
    def __init__(self, interestRate, bankName):
        self.interestRate = interestRate
        self.bankName = bankName

    def getInterestRate(self):
        return self.interestRate

    def getBankName(self):
        return self.bankName


class BankA(Bank):
    def getInterestRate(self):
        return self.interestRate


class BankB(Bank):
    def getInterestRate(self):
        return self.interestRate


class BankC(Bank):
    def getInterestRate(self):
        return self.interestRate


# service layer
class BankUtil:
    def queryInterestRate(self, bankObj):
        result = bankObj.getInterestRate()
        return result

    def queryAllInterestRate(self, bankObjList):
        result = []
        for bankObj in bankObjList:
            result.append(   (bankObj.getBankName(), bankObj.getInterestRate())    )
        return result

# main
# application layer
bank1 = BankA(0.04, 'BANK-A')
bank2 = BankB(0.0395, 'BANK-B')
bank3 = BankC(0.035, 'BANK-C')

#
bank_list = [bank1, bank2, bank3]

myapp = BankUtil()

print("welcome to bank checking system")
print("Here are three banks to choose from:")
print("Choose BankA, press A.")
print("Choose BankB, press B.")
print("Choose BankC, press C.")

"""
var = str(input("Please choose the bank that you want to check :"))

if var == 'A':
        print(f'The interest rate of this bank is {myapp.queryInterestRate(bank1):.3%}')
elif var == 'B':
        print(f'the interest rate of this bank is {myapp.queryInterestRate(bank2):.3%}')
elif var == 'C':
        print(f'the interest rate of this bank is {myapp.queryInterestRate(bank3):.3%}')
"""

#
data = myapp.queryAllInterestRate(bank_list)
for bankObj in data:
    print(bankObj[0], bankObj[1])

