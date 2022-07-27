"""
hybrid inheritance
"""


class Car:
    def accelerate(self):
        print('accelerate()')

    def brake(self):
        print('brake()')

    def turn(self):
        print('turn()')


class ElectricCar(Car):
    def recharge(self):
        print('recharge()')


class FuelCar(Car):
    def refill(self):
        print('refill()')


class HybridCar(ElectricCar,FuelCar):
    def switchMode(self):
        print('switchMode()')

# test
myHybridCar = HybridCar()
myHybridCar.switchMode()
myHybridCar.refill()
myHybridCar.recharge()
myHybridCar.accelerate()
myHybridCar.brake()
myHybridCar.turn()