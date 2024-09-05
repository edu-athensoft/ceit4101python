"""
My Bank Service
"""


class MyBankService:
    def queryInterestRate(self, bankObj):
        result = bankObj.getInterestRate()
        return result

    def queryMutilInterestRate(self, bankObjList):
        multiInterestRate = []
        for bank in bankObjList:
            multiInterestRate.append(bank.getInterestRate())
        return multiInterestRate
