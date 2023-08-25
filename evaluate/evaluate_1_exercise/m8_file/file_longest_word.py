"""

"""

# def printlist(mylist):
#     for item in mylist:
#         print(item)

def removepunc(word):
    word = word.replace('"','')
    if not word[-1].isalpha():
        return word[:-1]
    return word

# def clean(mylist):
#     size = len(mylist)
#     for i in range(size):
#         mylist[i] = removepunc(mylist[i])
#     return mylist

try:
    file = open("TextFileForQ8")

    words = file.read().split()
    # printlist(clean(content_list))

    # maxlen, longestword = 0, ''
    result = [[len(removepunc(words[i])), removepunc(words[i])] for i in range(len(words))]
    result.sort(reverse=True)
    print(result[0:3])

except FileNotFoundError as e:
    print(e)

finally:
    file.close()

