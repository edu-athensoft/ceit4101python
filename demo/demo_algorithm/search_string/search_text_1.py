"""
searching a pattern in a given text

Text        T
Pattern     P

assuming
T = 'aaaabaaaaaaab'
P = 'aaab'

We try a new algorithm other than KMP
Get the last char of P as lastCharP
Search lastCharP in T
if found lastCharP at position i, then comparing P with substring T[i-len(P)+1 : i]
if matched, then calculate the starting index of substring T[i-len(P)+1 : i]
  which is i-len(P)+1
if not matched, then search for the next position of lastCharP in T
  till the end

"""

class TextSearching:

    def __init__(self, text='', pattern=''):
        self.text = text
        self.pattern = pattern

    def getLastChar(self, mystr):
        if len(mystr) > 0:
            return mystr[-1]
        else:
            return None

    def findCharIndex(self, char, mystr):
        length = len(mystr)
        for i in range(length):
            if char == mystr[i]:
                return i

    def search(self):
        T = self.text
        P = self.pattern

        LENT = len(T)
        LENP = len(P)

        lastCharP = P[-1]

        # it = 0
        # find and match the last char
        for i in range(LENT):
            if lastCharP == T[i]:
                # print(i)

                # matching P in T
                it = i - LENP + 1
                isFound = True
                for j in range(LENP):
                    # print(f'P[{j}]={P[j]}, T[{it}]={T[it]}')

                    if P[j] == T[it]:
                        # print("i=", i, "it = ", it)
                        it += 1
                    else:
                        isFound = False
                        break

                if isFound:
                    print(f"Found a P in T at the position of {i-LENP+1}")

        else:
            print('Done')


    def isEqualString(self, s1, s2):
        if len(s1) != len(s2):
            return False

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
            else:
                return True

        return True

# main
myts = TextSearching('1111112','112')
# myts = TextSearching('abcabcfdaabcfbceabcfabc','abcf')
# myts = TextSearching('122122122122','12')

# result = myts.findCharIndex('a','bcdefabcd')
# print(result)

print(myts.text)
print(myts.pattern)
myts.search()
# result = myts.isEqualString('11','11')
# print(result)

