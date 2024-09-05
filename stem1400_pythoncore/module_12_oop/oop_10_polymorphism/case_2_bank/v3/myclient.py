"""
My client
provider:  XYZ Software Tech and Service Inc.
or
OpenSource, Customizable
"""

import banksys
import mysys


# main
bank1 = banksys.BankA(0.04)
bank2 = banksys.BankB(0.0395)
bank3 = banksys.BankC(0.035)

mysysapp = mysys.MyBankUtil()
# task of query interest rate of a single bank for multiple times
print("Query interest rate of BankA")
print(f'{mysysapp.queryInterestRate(bank1):.3%}')
print()

print("Query interest rate of BankB")
print(f'{mysysapp.queryInterestRate(bank2):.3%}')
print()

print("Query interest rate of BankC")
print(f'{mysysapp.queryInterestRate(bank3):.3%}')


# task of batch job
# at one time
bankList = [bank1, bank2, bank3]
# bankList = [BankA(0.04), BankA(0.04), BankA(0.04),BankB(0.0395),BankB(0.0395)]
result = mysysapp.queryMutilInterestRate(bankList)
print(result)
