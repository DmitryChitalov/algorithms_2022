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

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(0, len(nums), 2)]

nums = list(range(1000))


print("Test first " + str(timeit("func_1(nums)", globals=globals(), number=1000)))
print("Test second " + str(timeit("func_2(nums)", globals=globals(), number=1000)))

# Test first 0.09864220000235946
# Test second 0.015747000001283595
# Использование list comprehension и "шаг" 2 (нет необходимости проводить проверку) существенно сокращает время исполнения
