"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!

Основы. Д/р №1, задание №2
"""
from memory_profiler import memory_usage
from numpy import array


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(mem_diff)
        return res
    return wrapper


@decor
def func_1():
    my_list = []
    my_sum = 0

    for i in range(1, 100000, 2):
        my_list.append(i ** 3)

    for ind, n in enumerate(my_list):
        sum_one = 0
        while n:
            sum_one += n % 10
            n //= 10
        if sum_one % 7 == 0:
            my_sum += my_list[ind]


func_1()  # 1.6


@decor
def func_2():
    my_list = array([i ** 3 for i in range(1, 100000, 2)])
    my_sum = 0

    for ind, n in enumerate(my_list):
        sum_one = 0
        while n:
            sum_one += n % 10
            n //= 10
        if sum_one % 7 == 0:
            my_sum += my_list[ind]


func_2()  # 1.1

# Использование функции array, позволило сократить расход памяти
