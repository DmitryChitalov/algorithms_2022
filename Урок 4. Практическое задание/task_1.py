"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    """
    Оптимизация для упорядоченных массивов.
    Убрана проверка на четность, можно просто через 1 проходить по массиву.
    """
    new_arr = []
    for i in range(0, len(nums), 2):
        new_arr.append(i)
    return new_arr


def func_3(nums):
    """
    Оптимизация для упорядоченных массивов.
    Убрана проверка на четность, можно просто через 1 проходить по массиву.
    + с использованием list comprehension
    """
    return [num for num in range(0, len(nums), 2)]


nums = range(0, 1000)
print('Обычная реализация:')
print(
    timeit(
        "func_1(nums)",
        globals=globals(),
        number=10000))
print('Реализация с шагом 2')
print(
    timeit(
        "func_2(nums)",
        globals=globals(),
        number=10000))
print('Реализация с шагом 2, с использованием list comprehension')
print(
    timeit(
        "func_3(nums)",
        globals=globals(),
        number=10000))
