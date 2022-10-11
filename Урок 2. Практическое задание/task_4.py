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


def rowCount(n, el=1, i=0, sum=0):
    if i == n:
        print(f'сумма: {sum}')
        return
    else:
        sum = sum + el
        el /= -2
        return rowCount(n, el, i + 1, sum)


count = int(input('Введите n: '))
rowCount(count)
