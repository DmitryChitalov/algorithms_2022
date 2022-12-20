
from collections import defaultdict, namedtuple
import pickle
from memory_profiler import profile
from pympler import asizeof
from memory_profiler import memory_usage
from time import time


'''
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
'''


@profile
def recursion(num):
    def sum_elements(n, s=0, e = 1):
        if n == 0:
            return s
        else:
            s += e
            e /= -2
        return sum_elements(n-1, s, e)
    print(sum_elements(num))



@profile
def sum_elements_2(num):
    e = 1
    s = 0
    for i in range(num):
        s += e
        e /= -2
    return s


num = 900
recursion(num)
sum_elements_2(num)

''' Рекурсивные функции занимают больше места в памяти по сравнению с итеративными 
из-за постоянного добавления новых слоев в стек в памяти.

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13     25.9 MiB     25.9 MiB           1   @profile
    14                                         def recursion(num):
    15     26.4 MiB      0.3 MiB         502       def sum_elements(n, s=0, e = 1):
    16     26.4 MiB      0.1 MiB         501           if n == 0:
    17     26.4 MiB      0.0 MiB           1               return s
    18                                                 else:
    19     26.4 MiB      0.0 MiB         500               s += e
    20     26.4 MiB      0.1 MiB         500               e /= -2
    21     26.4 MiB      0.0 MiB         500           return sum_elements(n-1, s, e)
    22     26.4 MiB      0.0 MiB           1       print(sum_elements(num))


Filename: C:\algorithms_2022\6_1\task_1_3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    26     26.4 MiB     26.4 MiB           1   @profile
    27                                         def sum_elements_2(num):
    28     26.4 MiB      0.0 MiB           1       e = 1
    29     26.4 MiB      0.0 MiB           1       s = 0
    30     26.4 MiB      0.0 MiB         501       for i in range(num):
    31     26.4 MiB      0.0 MiB         500           s += e
    32     26.4 MiB      0.0 MiB         500           e /= -2
    33     26.4 MiB      0.0 MiB           1       return s



Process finished with exit code 0
'''







