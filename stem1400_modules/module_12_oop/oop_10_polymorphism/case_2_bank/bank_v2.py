"""
bank interest query app
version: v1
"""


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


class ClientApp:
    def queryInterestRate(self, bankObj):
        result = bankObj.getInterestRate()
        return result

    def queryMutilInterestRate(self, bankObjList):
        multiInterestRate = []
        for bank in bankObjList:
            multiInterestRate.append(bank.getInterestRate())
        return multiInterestRate


# main
bank1 = BankA(0.04)
bank2 = BankB(0.0395)
bank3 = BankC(0.035)

myapp = ClientApp()
# task of query interest rate of a single bank for multiple times
print("Query interest rate of BankA")
print(f'{myapp.queryInterestRate(bank1):.3%}')
print()

print("Query interest rate of BankB")
print(f'{myapp.queryInterestRate(bank2):.3%}')
print()

print("Query interest rate of BankC")
print(f'{myapp.queryInterestRate(bank3):.3%}')


# task of batch job
# at one time
bankList = [bank1, bank2, bank3]
# bankList = [BankA(0.04), BankA(0.04), BankA(0.04),BankB(0.0395),BankB(0.0395)]
result = myapp.queryMutilInterestRate(bankList)
print(result)


