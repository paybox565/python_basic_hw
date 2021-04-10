from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    started = False

    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel == 0:
            raise LowFuelError()

        self.started = True

    def move(self, distance: int):
        if self.fuel < distance*self.fuel_consumption:
            raise NotEnoughFuel()

        self.fuel -= distance*self.fuel_consumption


