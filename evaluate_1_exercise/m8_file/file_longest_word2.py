"""

"""


def removepunc(word):
    """
    remove double quote
    remove space, comma, semi-colon, dot
    :param word:
    :return: cleaned word
    """
    word = word.replace('"','').strip(' ,;.')
    # if not word[-1].isalpha():
    #     return word[:-1]
    return word

try:
    file = open("TextFileForQ8")

    words = list(map(lambda x: removepunc(x),file.read().split()))

    sizes = [len(word) for word in words]

    result = list(zip(*(sizes, words)))
    result.sort(reverse=True)


    print(result[0:3])

except FileNotFoundError as e:
    print(e)

finally:
    file.close()

