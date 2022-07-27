"""
method chaining

1. without chaining
"""

class Car:
    def start(self):
        print("start")

    def accelarate(self):
        print("accelarate")

    def brake(self):
        print("brake")

    def stop(self):
        print("stop")


#
mycar = Car()
mycar.start()
mycar.accelarate()
mycar.brake()
mycar.stop()
