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


def funct(k):
    n = k - 1
    return ((-1) ** n) / (2 ** n)


def recurs(n, summ = 0):
    if n != 0:
        summ = summ + funct(n)
        return recurs(n - 1, summ)
    else:
        return summ

print(recurs(3))

# Вариант 2
def recurs2(n):
    if n == 1:
        return funct(n)
    return funct(n) + recurs2(n - 1)

print(recurs2(3))

#Вариант 3

def recurs3(n):
    return funct(n) if (n == 1) else funct(n) + recurs3(n - 1)

print(recurs3(3))
