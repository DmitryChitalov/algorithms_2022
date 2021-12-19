#!+
"""
2021-12-18
Geekbrains. Факультет python-разработки
Студент: Папко Роман.
Четверть 1. Алгоритмы и структуры данных на Python. Базовый курс
Урок 2. Циклы. Рекурсия. Функции.
Домашнее задание 4.
"""
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


def summ(n, a = 1, sum = 0,count = 0):
    if n == 0:
        print(f'Количество элементов - {count}, их сумма - {sum}')
        return
    else:
        n -= 1
        count += 1
        sum += a
        summ(n, a/(-2), sum, count)

summ(int(input(f'Введите количество элементов: ')))
