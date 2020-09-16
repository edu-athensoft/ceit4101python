"""
function
- without returned value
- with returned value

"""

def showmenu():
    print("egg")
    print("chicken")
    print("fries")
    print("coke")
    print("dessert")
    return "OK"

# call it and lost returned value
showmenu()
print()

print(showmenu())
print()

# call it and keep returned value
isdone = showmenu()
print(isdone)
print(isdone+" -2nd")
print(isdone+" -3rd")




