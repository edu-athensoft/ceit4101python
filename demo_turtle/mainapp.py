
import turtle as turtle
import numpy as np
import os

# setup screen
wn = turtle.Screen()
# wn.bgcolor('black')

# turtle.home()
# p = turtle.position()
# print(p)


dots = np.arange(100)
print(dots)
np.random.shuffle(dots)
print(dots)


for x in dots:
    turtle.home()
    turtle.dot()

    s = np.random.rand();
    sign = 1
    if(s >0.5):
        sign = 1
    else:
        sign = -1

    s2 = np.random.rand();
    sign2 = 1
    if (s2 > 0.5):
        sign2 = 1
    else:
        sign2 = -1

    turtle.setpos(sign*100*np.random.rand(), sign2*100*np.random.rand())
    # turtle.fd(5*float(x)); turtle.dot(10, "blue"); turtle.fd(5*float(x))
    turtle.dot(10, "blue");
    # turtle.position()
    # turtle.heading()
turtle.done()

# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()



# tt.color('red', 'yellow')
# tt.begin_fill()
# while True:
#     tt.forward(200)
#     tt.left(170)
#     if abs(tt.pos()) < 1:
#         break
# tt.end_fill()
# tt.done()


