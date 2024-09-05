"""
bank system
provider:  ABC Financial Institute
"""


class Bank:
    def __init__(self, interestRate):
        self.interestRate = interestRate

    def getInterestRate(self):
        return self.interestRate


class BankA(Bank):
    # def getInterestRate(self):
    #     return self.interestRate
    pass


class BankB(Bank):
    # def getInterestRate(self):
    #     return self.interestRate
    pass


class BankC(Bank):
    # def getInterestRate(self):
    #     return self.interestRate
    pass
