"""Определение НОД"""


def first_method(a, b):
    """Цикл"""
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)


first_method(36, 60)


def second_method(a, b):
    """Рекурсия"""
    if b == 0:
        return a
    return second_method(b, a % b)


print(second_method(36, 60))


def third_method(a, b):
    """Тоже цикл"""
    while b != 0:
       a, b = b, a % b
    return a


print(third_method(36, 60))

