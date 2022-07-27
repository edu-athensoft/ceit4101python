"""
My Bank Service
"""


class MyBankService:
    def queryInterestRate(self, bankObj):
        return bankObj.getInterestRate()

    def queryAllInterestRate(self, bankObjList):
        allInterestRates = []
        for bank in bankObjList:
            allInterestRates.append((bank.getBankName(), bank.getInterestRate()))
        return allInterestRates

