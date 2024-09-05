# change the item(s) of a list

list_season = ['Spring11','Summer22','Fall33','Winter44']
# list_season[0] = 'Spring'
# list_season[1] = 'Summer'
# list_season[2] = 'Fall'
# list_season[3] = 'Winter'

print(list_season)

list_season[1:3] = ['Summer', 'Fall']
print(list_season)

# add one item
list_season.append("Rainy")
print(list_season)

list_season.extend(['Sunny','Rainy'])
print(list_season)




