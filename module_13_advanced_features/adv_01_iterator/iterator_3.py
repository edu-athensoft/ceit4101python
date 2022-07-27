"""

"""

class ColorsIterator:
    def __init__(self, colors):
        self.__data = colors
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__data):
            raise StopIteration

        # return the next data item
        dataItem = self.__data.data[self.__index]
        self.__index += 1
        return dataItem


class Colors:
    def __init__(self):
        self.data = [1,2,3]

    def __len__(self):
        return len(self.data)

    # adding this to make it iterable
    def __iter__(self):
        return ColorsIterator(self)


# main
colors = Colors()
for color in colors:
    print(color)

# test iterator
colors_iterator = iter(colors)
print(colors_iterator)
print(next(colors_iterator))
print(next(colors_iterator))
print(next(colors_iterator))
print(next(colors_iterator))
