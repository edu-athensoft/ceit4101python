# peaches is the number of peaches after eating on a certain day
peaches = 1
day = 9

while day > 0:
    peaches = 2 * (peaches+1)
    day -= 1

print(f"The monkey picked {peaches} peaches on the first day.")