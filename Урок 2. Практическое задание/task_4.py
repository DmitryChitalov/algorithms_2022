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

def summ(result=0, count_start=0, count_total=0):
    if count_start == 0:
        count_total = int(input('Введите количество элементов:'))
    if count_start < count_total:
        result = result + float(input('Введите число:'))
        return summ(result, count_start + 1, count_total)
    else:
        print(f'Количество элементов {count_total}, их сумма {result}')
        return

summ()
