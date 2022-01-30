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


def recur_sum(i, count=1, sum=1, num=1):
    if i == 0:
        print(f'Amount of elements - 0, sum = 0')
    if i == 1:
        print(f'Amount of elements - {count}, sum = {sum}')
        return
    else:
        num = (num/2)*-1
        sum += num
        count += 1
    return recur_sum(i-1, count, sum, num)


recur_sum(3)
