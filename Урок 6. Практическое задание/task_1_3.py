"""
Задание 1.3.
"""
# Алгоритмы Python. DZ_5.3
# сравнить операции  append

from memory_profiler import memory_usage
import numpy as np
from random import randint


def mem_usage(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение функции заняло {mem_diff} Mib")
        return res

    return wrapper


@mem_usage
def func():
    my_list = []
    for i in range(100000):
        my_list.append(randint(1, 1000))


# Вариант с numpy array
@mem_usage
def func_opt():
    my_array = np.array([])
    for i in range(100000):
        np.append(my_array, randint(1, 1000))


if __name__ == '__main__':
    func()
    func_opt()

"""
Выполнение функции заняло 1.79296875 Mib
Выполнение функции заняло 0.00390625 Mib

Массивы numpy занимают значительно меньше места в памяти,
но при этом могут заполняются медленнее, чем списки
"""
