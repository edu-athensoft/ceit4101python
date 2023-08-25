"""
Bank Service
"""
import bankdata


class BankService:
    def __init__(self):
        self.bankData = bankdata.bank_data

    def __queryInterestRate(self, bankObj):
        return bankObj.getInterestRate()

    def __queryAllInterestRate(self, bankObjList):
        records = []
        for bankObj in bankObjList:
            records.append((bankObj.getBankName(), bankObj.getInterestRate()))
        return records

    def __getInstanceByBankNo(self, bankNo):
        return self.bankData[bankNo]

    def __getInstances(self, bankNoList=[]):
        if len(bankNoList) == 0:
            bankNoList = list(self.bankData)

        bankObjList = []
        for bankNo in bankNoList:
            bankObjList.append(self.__getInstanceByBankNo(bankNo))
        return bankObjList

    def showInterestRate(self, bankNo):
        if bankNo in list(self.bankData):
            bankObj = self.__getInstanceByBankNo(bankNo)
            bankName = bankObj.getBankName()
            interestRate = self.__queryInterestRate(bankObj)
            print(f'Current Interest rate of {bankName} ==> {interestRate:.3%}\n')
        else:
            print('[ERROR] Invalid bank no.')

    def showInterestRateList(self):
        bankObjects = self.__getInstances()
        print('\n=== Table of Bank Interest Rate ===')
        for bankObj in bankObjects:
            print(f'{bankObj.getBankName()} : {bankObj.getInterestRate():.3%}')
        print()
