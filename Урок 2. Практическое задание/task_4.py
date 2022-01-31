"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""


def summ_n(x, amount_of_element):
    if amount_of_element != 0:
        number_of_row = float(input())
        return summ_n(x + number_of_row, amount_of_element - 1)
    else:
        print(f'сумма числе равна: {x}')


summ_n(0, int(input()))
