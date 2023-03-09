"""
iterator
"""


class Square:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.length:
            raise StopIteration

        self.current += 1
        return self.current ** 2


# test
square1 = Square(5)

for i in square1:
    print(i)
