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


def sum_sequence(step, number=1.0, sign=-1, sum_seq=0.0):
    if step == 0:
        return sum_seq
    sum_seq = sum_seq + number
    number = (number / 2) * sign
    step -= 1
    return sum_sequence(step, number, sign, sum_seq)


print(sum_sequence(3))

