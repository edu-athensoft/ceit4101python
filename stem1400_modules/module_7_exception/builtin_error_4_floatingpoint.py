"""
built-in error
FloatingPointError

https://www.cs.auckland.ac.nz/references/python/3.2.3-docs/library/fpectl.html

https://blog.airbrake.io/blog/python/floatingpointerror

notes:
the module fpectl is a must
"""
"""
>>> import fpectl
>>> import fpetest
>>> fpectl.turnon_sigfpe()
>>> fpetest.test()
overflow        PASS
FloatingPointError: Overflow

div by 0        PASS
FloatingPointError: Division by zero
[ more output from test elided ]
>>> import math
>>> math.exp(1000)
Traceback (most recent call last):
File "<stdin>", line 1, in ?
FloatingPointError: in math_1
"""




