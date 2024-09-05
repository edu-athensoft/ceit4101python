"""
string method
expandtabs()
expandtabs(tabsize) -  replaces tab character with spaces
tabsize	Optional. A number specifying the tabsize. Default tabsize is 8
"""

s1 = "abc11\t\tdef222\tghi333"
print(s1)

s2 = s1.expandtabs(tabsize=2)
print(s2)

