"""
python dir

Get Current Directory
"""

import os

d1 = os.getcwd()
print(d1, type(d1))


# get it as bytes object
# DeprecationWarning:
# The Windows bytes API has been deprecated,
# use Unicode filenames instead

d2 = os.getcwdb()
print(d2, type(d2))