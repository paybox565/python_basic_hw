"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    increased_numbers = []
    for number in numbers:
        increased_numbers.append(number ** 2)

    return increased_numbers


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    result_numbers = []
    if filter_type == "odd":
        for number in numbers:
            if number % 2 != 0:
                result_numbers.append(number)
    elif filter_type == "even":
        for number in numbers:
            if number % 2 == 0:
                result_numbers.append(number)
    elif filter_type == "prime":
        for number in numbers:
            if is_prime(number):
                result_numbers.append(number)

    return result_numbers
