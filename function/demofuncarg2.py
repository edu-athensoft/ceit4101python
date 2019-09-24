# default argument

def greet(name, msg = "Good morning!"):
   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")