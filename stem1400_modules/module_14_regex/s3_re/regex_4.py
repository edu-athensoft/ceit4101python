"""
regex
re.split()

Counting how many words (tokens)

Application scenarios:
1. word limits: by char, by words
2. word statistics (counting)
3. AI Text-to-Speech  (charge by token)
4. AI ChatGPT (charge by token)
5. Text Analysis (in SEO)

"""
import re

mystr = "The re.split()   method splits  the  string where there is a   match and returns a list of strings where the splits have occurred."
pattern = r"\s+"

tokens = re.split(pattern, mystr)
print(len(tokens))
