"""
Client of LearningApp

Access class variables in an instance method
"""

from module_11_oop.study.Learning import *

# test class variable
worker1 = Worker('Tom',20)
print()

worker2 = Worker('Jim',22)
print()

print("worker1.score =",worker1.score)
print("worker2.score =",worker2.score)
print("Worker.score =",Worker.score)
print()

worker1.score = 1
print("worker1.score =",worker1.score)
print("worker2.score =",worker2.score)
print("Worker.score =",Worker.score)
print()

worker2.score = 2
print("worker1.score =",worker1.score)
print("worker2.score =",worker2.score)
print("Worker.score =",Worker.score)
print()

Worker.score = 3
print("worker1.score =",worker1.score)
print("worker2.score =",worker2.score)
print("Worker.score =",Worker.score)
