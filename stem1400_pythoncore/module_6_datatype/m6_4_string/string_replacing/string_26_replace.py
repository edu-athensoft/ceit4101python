"""
string method - replace(original, new [, times] )

A string is immutable.
"""

# case 1.
song = "cold, cold heart"
# replace 'cold' with 'hurt'
res = song.replace('cold', 'hurt')
print(res)

# case 2.
str1 = "a b c d e f g"
# "a,b,c,d,e,f,g"

# print('====')
# print(str1.replace(' ',';'))
# print('====')


# option 1.
s2_list = str1.split()
print(s2_list)
res = ','.join(s2_list)
print(res)


# option 2.
res = str1.replace(' ',',')
print(res)



# case 3.
print("case 3.")
song = "let it be, let it be, let it be"

# let -> so
res = song.replace('let', 'so', 1)
print(res)

res = song.replace('let', 'so', 2)
print(res)
