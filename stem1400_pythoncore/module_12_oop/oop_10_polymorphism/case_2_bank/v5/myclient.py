"""
My client
"""

import banksys
import mysys

# settings
BANK_NO_LIST = ['1', '2', '3']
bankService = mysys.MyBankService()


def getInstanceByBankNo(bankNo):
    bankObj = None
    if bankNo == '1':
        bankObj = banksys.BankA(0.04)
    if bankNo == '2':
        bankObj = banksys.BankB(0.0395)
    if bankNo == '3':
        bankObj = banksys.BankC(0.035)
    return bankObj


def showInterestRate(bankNo):
    bankObj = getInstanceByBankNo(bankNo)
    bankName = bankObj.bankName
    interestRate = bankService.queryInterestRate(bankObj)
    print(f'Current Interest rate of {bankName} ==> {interestRate:.3%}\n')


def showAllInterestRate(bankNoList):
    bankObjList = []
    for bankNo in bankNoList:
        bankObjList.append(getInstanceByBankNo(bankNo))
    interestRateRecords = bankService.queryAllInterestRate(bankObjList)

    print('\n=== Table of Bank Interest Rate ===')
    for record in interestRateRecords:
        print(f'{record[0]} : {record[1]:.3%}')
    print()


def main():
    # head
    print("=======================================")
    print("===     My Bank Checking System     ===")
    print("===         Version 1.0             ===")
    print("=======================================")

    # two-level menu
    while True:
        print()
        print("<<< Main menu >>>")
        print("[S] Query for interest rate of a single bank")
        print("[A] Query for all bank interest rates")
        print("[Q] Quit")
        print("Please choose an option:", end='')
        optionCode = input()

        if optionCode.upper() == 'Q':
            print('\nBye!')
            break

        if optionCode.upper() == 'S':
            while True:
                print()
                print("=== Bank List ===")
                print("[1] Bank-A")
                print("[2] Bank-B")
                print("[3] Bank-C")
                print("[Q] Return")

                print("Please choose a bank:", end='')
                bankNoOption = input()

                if bankNoOption.upper() == 'Q':
                    break

                if bankNoOption in BANK_NO_LIST:
                    showInterestRate(bankNoOption)

        if optionCode.upper() == 'A':
            showAllInterestRate(BANK_NO_LIST)


# main logic
if __name__ == '__main__':
    main()
