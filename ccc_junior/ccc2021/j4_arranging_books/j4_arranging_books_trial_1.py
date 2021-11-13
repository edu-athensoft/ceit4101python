"""
CCC 2021 Junior
J4. Arranging books

S -> L prior to S -> M
"""

num_swap = 0


def swap(mylist, x, y):
    global num_swap
    tmp = mylist[x]
    mylist[x]=mylist[y]
    mylist[y]= tmp
    num_swap +=1


books = list(input())
N = len(books)
for i in range(N-1):
    if books[i] <= books[i+1]:
        continue
    swap(books, i, i+1)
    i -= 1

print(num_swap)




