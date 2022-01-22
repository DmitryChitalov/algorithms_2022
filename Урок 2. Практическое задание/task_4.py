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


def seq(n, sum_seq=0, r=1):
    if n == 0:
        return print(f'Сумма ряда: {sum_seq}')
    else:
        sum_seq += r
    return seq(int(n)-1, sum_seq, r * (-1 / 2))


x = input('Введите кол-во элементов ряда: ')
seq(x)