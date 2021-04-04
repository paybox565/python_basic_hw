"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    print('Fuel level is too low')


class NotEnoughFuel(Exception):
    print('Not enough fuel')


class CargoOverload(Exception):
    print('The cargo is too heavy')
