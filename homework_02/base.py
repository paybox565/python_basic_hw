from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    started = False

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        try:
            self.fuel > 0
        except Exception:
            raise LowFuelError
        else:
            self.started = True

    def move(self):
        try:
            self.fuel >= self.fuel_consumption
        except Exception:
            raise NotEnoughFuel
