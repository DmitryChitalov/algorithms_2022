"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""


def funct(k):
    n = k - 1
    return ((-1) ** n) / (2 ** n)


def recurs(n, summ=0):
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


# Вариант 3

def recurs3(n):
    return funct(n) if (n == 1) else funct(n) + recurs3(n - 1)


print(recurs3(3))
