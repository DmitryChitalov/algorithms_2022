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


def sum_of_elements(n: int, following: float = 1, carry: float = 0):
    if n == 0:
        return print(carry)
    else:
        carry += following
    sum_of_elements(n-1, following / -2, carry)


if __name__ == '__main__':
    print(sum_of_elements(5))
