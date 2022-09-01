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
import sys
sys.setrecursionlimit(10000)
def row_recursion(i, row_sum = 1, number = 1, count = 1):
    if i == 1:
        return row_sum, count
    else:
        number = number/2
        row_sum = row_sum - number
        return row_recursion(i - 1, row_sum, number * -1, count + 1)

print(row_recursion(9998))
