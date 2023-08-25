"""
Quiz 313
q3

There is a login program. User inputs username and password,
and then the system checks if username and password match
the credentials stored in the system.

The credential in the system is as username: admin, password: 12345
If the username and password that user inputs match both,
then the system outputs 'Login successfully!'; if not and only
the username matches, then the system outputs 'Wrong password!';
otherwise the system outputs 'No such username. Please try again!'

Please write a program to solve the above problem.
Hint:	Please save your code in the file naming as stem1401_quiz313_q3_yourname.py

"""

print("LOGIN")
username = input("Please enter your username")
password = int(input("Please enter your password"))

usernameAdmin = "admin"
passwordAdmin = 12345

message = None

if usernameAdmin == username and passwordAdmin == password:
    message = "Login successfully"
elif username != usernameAdmin and password != passwordAdmin:
    message = "NOTHING IS RIGHT"
elif username != usernameAdmin:
    message = "No such username. Please try again!"
elif password != passwordAdmin:
    message = "Wrong password"
else:
    message = "No message"

print(message)
