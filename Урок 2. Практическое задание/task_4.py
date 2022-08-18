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


def count(num: int, list_of_numbers: list, result: float = 0, iter_number: int = 1):
    iter_number = iter_number
    if num > 1:
        result += list_of_numbers[0]
        num -= 1
        iter_number += 1
        count(num, list_of_numbers[1:], result, iter_number)
    else:
        result += list_of_numbers[0]
        print(f'Количество элементов - {iter_number}, их сумма - {result}')

count(int(input('Сколько чисел будет в последовательности? ')), list(map(float, input('Введите числа: ').split())))
