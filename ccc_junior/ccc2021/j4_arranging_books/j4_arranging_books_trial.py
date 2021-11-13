"""
CCC 2021 Junior
J4. Arranging books

"""

books = 'LLSLM'

NumL = 0
NumM = 0
NumS = 0

for book in books:
    if book == 'L':
        NumL += 1
    elif book == 'M':
        NumM += 1
    else:
        NumS +=1
# print(NumL, NumM, NumS)

sectionL = books[:NumL]
sectionM = books[NumL:NumL+NumM]
sectionS = books[NumL+NumM]
# print(sectionL,sectionM,sectionS)

def getNonChar(mystr, char):
    n = 0
    for c in mystr:
        if char!=c:
            n +=1
    return n


def getChar(mystr, char):
    n = 0
    for c in mystr:
        if char==c:
            n += 1
    return n

non1 = getNonChar(sectionL,'L')
# print(non1)

non2 = getNonChar(sectionM,'M')
# print(non2)


n1 = getChar(sectionL,'M')
n2 = getChar(sectionM,'L')

result = non1 + non2 - min(n1, n2)
print(result)







