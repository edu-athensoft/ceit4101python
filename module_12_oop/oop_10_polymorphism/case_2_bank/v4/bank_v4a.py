"""
bank interest
version: v4
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


class BankUtil:
    def queryInterestRate(self, bankObj):
        result = bankObj.getInterestRate()
        return result

    def queryAllInterestRate(self, bankObjList):
        result = []
        for bankObj in bankObjList:
            result.append( bankObj.getInterestRate() )
        return result

# main
bank1 = BankA(0.04)
bank2 = BankB(0.0395)
bank3 = BankC(0.035)

#
bank_dict = {
    'a': bank1,
    'b': bank2,
    'c': bank3
}

myapp = BankUtil()

print("welcome to bank checking systheme")
print("There is three banks that you can choose:")
print("a)BANK A")
print("b)BANK B")
print("c)BANK C")

var = str(input("Please choose the bank that you want to check :"))

print("the interest rate of this bank is:")

"""
if var == 'a':
    print(f'{myapp.queryInterestRate(bank1):.3%}')
elif var == 'b':
    print(f'{myapp.queryInterestRate(bank2):.3%}')
elif var == 'c':
    print(f'{myapp.queryInterestRate(bank3):.3%}')

else:
    print("please input a,b or c")
"""

# bank_object = bank_dict[var]
# result = myapp.queryInterestRate(bank_object)
# print(f'{result:.3%}')

result = myapp.queryInterestRate(bank_dict[var])
print(f'{result:.3%}')

# print(f'{myapp.queryInterestRate(bank_dict[var]):.3%}')

print("Thanks for using bank util")


# query all bank interest rates
bank_list = list(bank_dict)
# print(bank_list)
bankObject_list = []
for bank in bank_list:
    bankObject_list.append(bank_dict[bank])

result = myapp.queryAllInterestRate(bankObject_list)
for interest in result:
    print(interest)


