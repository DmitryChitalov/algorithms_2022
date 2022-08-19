"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def geometric_progression(n):
    if n == 1:
        return 1
    return (-0.5) ** (n - 1) + geometric_progression(n - 1)

# или в более коротком варианте
def geometric_progression_short(n):
    return (-0.5) ** (n - 1) + geometric_progression(n - 1) if n else 0

print(geometric_progression(3))
print(geometric_progression(200)) # сумма должна стремиться к 2/3, так что похоже на правду
