"""
method chaining

1. without chaining
"""

class Car:
    def start(self):
        print("start")
        return self

    def accelarate(self):
        print("accelarate")
        return self

    def brake(self):
        print("brake")
        return self

    def stop(self):
        print("stop")
        return self


#
mycar = Car()
mycar.start().accelarate().brake().stop()
