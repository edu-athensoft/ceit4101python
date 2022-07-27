"""
bank system entities
"""


class Bank:
    def __init__(self, bankName, interestRate):
        self.__bankName = bankName
        self.__interestRate = interestRate

    def getInterestRate(self):
        return self.__interestRate

    def getBankName(self):
        return self.__bankName


class BankA(Bank):
    def __init__(self, bankName='BankA', interestRate=0):
        super().__init__(bankName, interestRate)


class BankB(Bank):
    def __init__(self, bankName='BankB', interestRate=0):
        super().__init__(bankName, interestRate)


class BankC(Bank):
    def __init__(self, bankName='BankC', interestRate=0):
        super().__init__(bankName, interestRate)
