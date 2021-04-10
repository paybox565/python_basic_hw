"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0

    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int = 0, max_cargo: int = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, weight: int):
        if self.max_cargo < self.cargo + weight:
            raise CargoOverload()

        self.cargo += weight

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0

        return current_cargo
