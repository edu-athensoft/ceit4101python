"""
Guessing number version 1.0

problems:
1. how to generate a random number/integer within a given range
2. how to validate the number and make it within your upper and lower bound
3. comparing your current number with the answer
    case #1: too small
    case #2: too big
    case #3: bingo
4. max 5 times
    failed for 5 times -> get "???"
    won within 5 times -> get "???"
5. difficulty problem
   fixed difficulty                     (version 1.0)
   adjustable difficulty                (version 1.1)
6. the number of turns you may play     (version 2)
"""


import random


def generate_answer():
    answer = random.randrange(1,101)
    return answer


def set_difficulty():
    chances = 5
    return chances


def get_valid_number():
    x = None
    while True:
        myinput = input("enter a number (1-100):")

        # validate myinput
        if myinput.isdigit():
            x = int(myinput)
            if x > 100 or x < 1:
                print("Warning: Please input a valid number!")
            else:
                # print("Your input is {}".format(x))
                break
        else:
            print("Warning: Please input a valid number!")
    return x


def compare(x, answer):
    flag = False
    if x > answer:
        print("Too big")
    elif x < answer:
        print("Too small")
    else:
        print("bingo")
        flag = True
    return flag


# main program, main logic
answer = generate_answer()
print("answer =", answer)

chances = set_difficulty()

for i in range(chances):
    x = get_valid_number()
    if compare(x, answer):
        break
    else:
        print("You have {} chances left".format(chances - i - 1))
    print()

