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
        if pos == -1:
            break
        pos_list.append(pos)
        start_pos = pos + len_substring
    return pos_list


def replaceSubstring(source, old, new, pos):
    source = source[:pos] + new + source[pos+len(old)+1:]
    return source


# rules
rule1 = ('AA','AB')
rule2 = ('AB', 'BB')
rule3 = ('B', 'AA')
rules = (rule1, rule2, rule3)

# input
S = 4
I = 'AB'
F = 'AAAB'

# process
for step in range(S):
    for rule in rules:
        source = I
        substring = rule[0]
        results = findAllSubstring(source, substring)
        print(rule, source, substring, results)
        if not results:
            continue

        for result in results:
            pos = result
            source = replaceSubstring(source, rule[0], rule[1], pos)
            print(">>"+source)
    print()


