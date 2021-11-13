"""
CCC 2021 Junior
J4. Arranging books

Resources: 0.836s, 10.06 MB
Maximum runtime on single test case: 0.292s
Final score: 15/15 (7.0/7 points)
"""


class Section:
    def __init__(self):
        self.nl = 0
        self.nm = 0
        self.ns = 0

    def add(self, book):
        if book == 'L':
            self.nl += 1
        elif book == 'M':
            self.nm += 1
        elif book == 'S':
            self.ns += 1
        else:
            pass


books = input()
allsection = Section()
for book in books:
    allsection.add(book)

lsec = Section()
msec = Section()
ssec = Section()

index = 0
for i in range(allsection.nl):
    lsec.add(books[index])
    index += 1

for i in range(allsection.nm):
    msec.add(books[index])
    index += 1

for i in range(allsection.ns):
    ssec.add(books[index])
    index += 1

result = (lsec.nm + lsec.ns) + (msec.nl + msec.ns) - min(lsec.nm, msec.nl)
print(result)
