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


def sum_recurs(null, one, count_number, summa):
    if null == count_number:
        print(f'Количество элементов - {count_number}, их сумма - {summa}')
    elif null < count_number:
        return sum_recurs(null + 1, one / 2 * -1, count_number, summa + one)


count = int(input('Введите количество желаемых элементов: '))
null = 0
one = 1
sum_recurs(null, one, count, 0)