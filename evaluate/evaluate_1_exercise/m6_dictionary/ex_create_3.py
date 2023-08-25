"""
module 6.       datatype
chapter 6-6.    dictionary

Question:
3. Write a program to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Hints:

"""

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

dict4 = {}
for d in (dict1, dict2, dict3):
    dict4.update(d)

print(dict4)
