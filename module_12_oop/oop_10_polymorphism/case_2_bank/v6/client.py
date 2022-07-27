"""
My client
"""

from bankservice import *

# settings
bankService = BankService()


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

                bankService.showInterestRate(bankNoOption)

        if optionCode.upper() == 'A':
            bankService.showInterestRateList()


# main logic
if __name__ == '__main__':
    main()
