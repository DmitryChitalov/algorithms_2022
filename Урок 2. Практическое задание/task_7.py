"""
2021-12-20
Geekbrains. Факультет python-разработки
Студент: Папко Роман.
Четверть 1. Алгоритмы и структуры данных на Python. Базовый курс
Урок 2. Циклы. Рекурсия. Функции.
Домашнее задание 6.
"""
"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def sum_n(n):
    if n == 1:
        return n
    else:
        return n + sum_n(n-1)


x = 100
if sum_n(x) == x * (x+1) / 2:
    print(f'1+...+{x} = {x} * ({x}+1) / 2  is  {sum_n(x) == x * (x+1) / 2} ')
else:
    print(f'1+...+{x} = {x} * ({x}+1) / 2  is  {sum_n(x) == x * (x+1) / 2} ')
