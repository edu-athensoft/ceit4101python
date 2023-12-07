"""
filtering duplicated chinese characters
"""

import char_sort_by_stroke as charsort

INPUT_FILE = "raw_char_hsk_4.txt"
OUTPUT_FILE = "sorted_char_hsk4.txt"

with open(INPUT_FILE, 'rt', encoding='UTF-8') as f:
    mystr = f.read()
    # print(mystr)


def get_char_set(char_seq):
    myset = set()
    for char in char_seq:
        if char and char != '\n':
            # print(f"{char}, unicode={ord(char)}")
            myset.add(char)
    return myset


def get_char_dict(char_seq):
    mydict = {}
    for char in char_seq:
        if char and char != '\n':
            mydict[ord(char)] = char
    return mydict


def sort_by_unicode(char_dict):
    results = sorted(char_dict)
    for code in results:
        print(f"{code} -> {char_dict[code]}")


def sort_by_stroke(list_str):
    return charsort.sort_by_strokes(list_str, model='total')

# my_char_dict = get_char_dict(mystr)
# sort_by_unicode(my_char_dict)


my_char_set = list(get_char_set(mystr))

results = sort_by_stroke(my_char_set)

# counting characters
print(len(results))


# save to file
with open(OUTPUT_FILE, 'w', encoding='UTF-8') as f:
    for char in results:
        f.write(char+"\n")


