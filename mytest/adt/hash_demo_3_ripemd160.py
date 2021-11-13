"""
hash algorithm: ripemd160

Issue
How to correct TypeError: Unicode-objects must be encoded before hashing?

original source:
https://stackoverflow.com/questions/7585307/how-to-correct-typeerror-unicode-objects-must-be-encoded-before-hashing
"""


import hashlib

h = hashlib.new('ripemd160')

words = "Nobody inspects the spammish repetition"
words = words.encode("utf-8")

h.update(words)

v1 = h.hexdigest()
print(v1)

