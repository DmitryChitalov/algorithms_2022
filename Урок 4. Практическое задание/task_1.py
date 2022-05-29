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


def create_list(n):
    return [el for el in range(n)]


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


if __name__ == '__main__':

    nums = create_list(10000)
    print(timeit('func_1(nums)', number=10000, globals=globals()))
    print(timeit('func_2(nums)', number=10000, globals=globals()))

"""
Для создания списка использовал list comprehensions, в этом случае отсутствует 
создание пустого списка, а также не задействует метод append, поэтому функция работате быстрее.
"""
