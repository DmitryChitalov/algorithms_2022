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


def get_sum_deg(st_qty, end_qty=0, sum_1=0.0, prev_el=-2.0):
    sum_cur = sum_1
    start = st_qty
    end = end_qty
    prev = prev_el
    if start == 0:
        print(f'Количество элементов: {end_qty}, их сумма = {sum_cur}')
    else:
        sum_cur = sum_cur + prev_el / -2
        start -= 1
        end += 1
        return get_sum_deg(start, end, sum_cur, prev / -2)


get_sum_deg(int(input('Введите количество элементов:  ')))
