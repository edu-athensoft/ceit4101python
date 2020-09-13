"""
2. Data Analysis and Sorting (20')
"""

def getmax(x,y):
    if x > y:
        return x
    else:
        return y


results = [['Robert Master',220,340],
          ['Montreal Sprite',320,270],
          ['Smart Maker',115,405],
          ['Nova Robert',450,480],
          ['10 Stars',100,330]]

# calculate the higher score for each team
for team in results:
    team.append(getmax(team[1],team[2]))

# print(results)

# sorting in descending order
results.sort(key=(lambda item: item[3]), reverse=True)
# print(results)

# output result
count = 0
for team in results:
    if count < 3:
        # print(team)
        print(f"Place #{count+1} is: {team[0]} at {team[3]}")
    count += 1


