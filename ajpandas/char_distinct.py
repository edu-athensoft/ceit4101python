"""
remove duplicated char from B comparing with A
"""

import char_sort_by_stroke as charsort

FILE_1 = "sorted_char_hsk1.txt"
FILE_2 = "sorted_char_hsk2.txt"
FILE_3 = "sorted_char_hsk3.txt"
FILE_4 = "sorted_char_hsk4.txt"
FILE_5 = "sorted_char_hsk5.txt"

OUTPUT_FILE_1 = 'distinct_sorted_char_hsk_1.txt'
OUTPUT_FILE_2 = 'distinct_sorted_char_hsk_2.txt'
OUTPUT_FILE_3 = 'distinct_sorted_char_hsk_3.txt'
OUTPUT_FILE_4 = 'distinct_sorted_char_hsk_4.txt'
OUTPUT_FILE_5 = 'distinct_sorted_char_hsk_5.txt'


# remove duplicated char from B
def load(file):
    char_set = set()
    with open(file, 'rt', encoding="UTF-8") as f:
        for line in f:
            if line != '\n':
                # print(line.strip())
                char_set.add(line.strip())
    return char_set


# test
set1 = load(FILE_1)
set2 = load(FILE_2)
set3 = load(FILE_3)
set4 = load(FILE_4)
set5 = load(FILE_5)

# hsk_2
print("HSK 2")
distinctSet2 = set2 - set1
sortedCharSet2_distinct = charsort.sort_by_strokes(list(distinctSet2), model='total')
print(sortedCharSet2_distinct)


# hsk_3
print("HSK 3")
distinctSet3 = set3 - set2 - set1
sortedCharSet3_distinct = charsort.sort_by_strokes(list(distinctSet3), model='total')
print(sortedCharSet3_distinct)


# hsk_4
print("HSK 4")
distinctSet4 = set4 - set3 - set2 - set1
sortedCharSet4_distinct = charsort.sort_by_strokes(list(distinctSet4), model='total')
print(sortedCharSet4_distinct)


# hsk_5
print("HSK 5")
distinctSet5 = set5 - set4 - set3 - set2 - set1
sortedCharSet5_distinct = charsort.sort_by_strokes(list(distinctSet5), model='total')
print(sortedCharSet5_distinct)



# output
def save(output_file, sortedCharSet_distinct):
    with open(output_file, 'w', encoding="UTF-8") as f:
        for char in sortedCharSet_distinct:
            f.write(char+"\n")


# save to file
# save(OUTPUT_FILE_2, sortedCharSet2_distinct)
# save(OUTPUT_FILE_3, sortedCharSet3_distinct)
# save(OUTPUT_FILE_4, sortedCharSet4_distinct)
# save(OUTPUT_FILE_5, sortedCharSet5_distinct)

a = len(set1)
b = len(sortedCharSet2_distinct)
c = len(sortedCharSet3_distinct)
d = len(sortedCharSet4_distinct)
e = len(sortedCharSet5_distinct)

print(a, b, c, d, e)

print((a+b+c+d+e))