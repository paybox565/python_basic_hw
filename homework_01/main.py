"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(numbers):
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
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
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
            if number % 2 == 0:
                result_numbers.append(number)
    elif filter_type == "even":
        for number in numbers:
            if number % 2 != 0:
                result_numbers.append(number)
    elif filter_type == "prime":
        for number in numbers:
            if number > 1:
                if is_prime(number):
                    result_numbers.append(number)
                    print(number, "case 2 is a prime number")
            else:
                print(number, "case 3 is not a prime number")
    else:
        return "Unknown type"

    return result_numbers


list_example = (range(1, 30))
# result = power_numbers(list_example)
result = filter_numbers(list_example, PRIME)
print(result)
