"""
bank system
"""


class Bank:
    def __init__(self, interestRate, bankName):
        self.interestRate = interestRate
        self.bankName = bankName

    def getInterestRate(self):
        return self.interestRate

    def getBankName(self):
        return self.bankName


class BankA(Bank):
    def __init__(self, interestRate, bankName='Bank-A'):
        super().__init__(interestRate, bankName)


class BankB(Bank):
    def __init__(self, interestRate, bankName='Bank-B'):
        super().__init__(interestRate, bankName)


class BankC(Bank):
    def __init__(self, interestRate, bankName='Bank-C'):
        super().__init__(interestRate, bankName)
