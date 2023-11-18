"""
find max from a list
[1, 3, 7, 4, 2, 5, 6]

N = 7, max([1, 3, 7, 4, 2, 5, 6])
[1], [3, 7, 4, 2, 5, 6]
if 1 > max([3, 7, 4, 2, 5, 6])
  return 1
else
  return max([3, 7, 4, 2, 5, 6])


N = 6, max([3, 7, 4, 2, 5, 6])
[3], [7, 4, 2, 5, 6]
if 3 > max([7, 4, 2, 5, 6])
  return 1
else
  return max([7, 4, 2, 5, 6])
"""


def find_max(restlist):
    if len(restlist) == 1:
        return restlist[0]

    max_rest = find_max(restlist[1:])
    if restlist[0] > max_rest:
        return restlist[0]
    else:
        return max_rest


# test
mylist = [1, 3, 7, 4, 2, 5, 6]
print(find_max(mylist))
