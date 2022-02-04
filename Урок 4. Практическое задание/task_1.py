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



def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


nums = [i for i in range(1000)]


print(timeit("func_1(nums)", globals=globals(), number=1000))

# В функции func_2 произведена оптимизация кода.
# Скорость выполнение быстрее, чем в функции func_1,
# т.к. все результаты сразу возвращаются в новый список,
# без использования метода append.
print(timeit("func_2(nums)", globals=globals(), number=1000))


