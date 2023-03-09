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
        self.data = ["red", "green", "blue"]

    def __len__(self):
        return len(self.data)


# main
colors = Colors()
colors_iterator = ColorsIterator(colors)
print(colors_iterator)

for color in colors_iterator:
    print(color)
