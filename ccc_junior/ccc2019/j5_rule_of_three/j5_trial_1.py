"""
J5 trial
"""


# find all substrings in a source string
# return a list of all possible positions of the substring
def findAllSubstring(source, substring):
    start_pos = 0
    pos_list = []
    len_substring = len(substring)
    while start_pos < len(source):
        pos = source.find(substring, start_pos)
        pos_list.append(pos)
        start_pos = pos + len_substring
    return pos_list


def replaceSubstring(source, old, new, pos):
    source = source[:pos] + new + source[pos+len(old)+1:]
    return source

# test
source = 'ABBAABAAABBA'
target = 'BA'
result = findAllSubstring(source, target)
print(result)

# test
source = 'ABBAABAAABBA'
old = 'AB'
new = 'CC'
pos = source.find(old)
result = replaceSubstring(source, old, new, pos)
print(result)

source = result
pos = source.find(old, pos)
result = replaceSubstring(source, old, new, pos)
print(result)

source = result
pos = source.find(old, pos)
result = replaceSubstring(source, old, new, pos)
print(result)