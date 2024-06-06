"""
string method - startswith(), endswith()

string.startswith()
return True if a string starts with the specified prefix(string)
return False if not

string.endswith()
return True if a string ends with the specified suffix(string)
return False if not
"""


text1 = "Python is easy"
text2 = "Java is hard"
text3 = "Python is awesome"
text4 = "Java is powerful"
text5 = "Javascript is easy"

# result = text1.startswith("Python")
# print(f"result = {result}")
#
# result = text2.startswith("Python")
# print(f"result = {result}")
#
# result = text3.startswith("Python")
# print(f"result = {result}")
#
# result = text4.startswith("Python")
# print(f"result = {result}")


# pick up all sentences which starts with 'Python'
mytext = [text1,text2,text3,text4]

print("=== All sentences starting with 'Python' ===")
for text in mytext:
    flag = text.startswith('Python')
    if flag :
        # print(f"{text} [{flag}]")
        print(f"{text}")
    else:
        pass

n = -1
bool1 = n > 0
if bool1:
    print ("n is a positive number")
else:
    print("n is a negative number")


# [Homework]
# pick up all languages easy to learn



