"""
sudoku loader
"""

# data
def load():
    with open("sudoku.txt") as f:
        puzzles = f.readlines()
        puzzles = list(set(puzzles))
        num = len(puzzles)

    for i in range(num):
        puzzles[i]= puzzles[i].strip()
    return puzzles, num


def generate(str_puzzle):
    count = 0
    for num in str_puzzle:
        if num == '.':
            num = '0'
        print(num, end="\t")
        count += 1
        if count%9 == 0:
            print()

# main
print("loading ...")
puzzles, num = load()
print(f"{num} puzzles loaded.")
for p in puzzles:
    print(p)
print()

print("generating ...")
for p in puzzles:
    generate(p)
    print()



