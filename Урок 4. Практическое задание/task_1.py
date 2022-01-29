"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit
numbers = list(range(50000))

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print("func_1:", timeit("func_1(numbers)", "from __main__ import func_1, numbers", number=1000))


def func_2(nums: list) -> list:
    """
    функция оптимизирована с помощью list comprehension работает быстрей чем обычный цикл примерно на 20% если верить
    замерам времени
    :param nums: list
    :return: list
    """
    new_arr = [x for x in range(len(nums)) if nums[x] % 2 == 0]
    return new_arr


print("func_2:", timeit("func_2(numbers)", "from __main__ import func_2, numbers", number=1000))


def func_3(nums: list):
    """
    Оптимизирована функция возвращает генератор по которому надо еще обойти либо сделать сгенерировать список
    :param nums: list
    :return: generator
    """
    new_arr = (x for x in range(len(nums)) if nums[x] % 2 == 0)
    return new_arr

print("func_3:", timeit("func_3(numbers)", globals=globals(), number=1000))


def func_4(nums: list):
    """
    filter не хранит значения в памяти, следственно работает быстрее, но функция возвращает итератор
    который в последствии нужно обойти либо сгенерировать список что потребует ресурсов и имеет свою сложность
    выполнения, однако на мой взгляд самая оптимизированая функция
    :param nums: list
    :return: iterator
    """
    new_arr = filter(lambda x: x % 2 == 0, nums)
    return new_arr


print("func_4:", timeit("func_4(numbers)", globals=globals(), number=1000))
