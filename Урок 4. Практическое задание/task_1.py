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
test_lst = [n for n in range(51)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_lst = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_lst


print(timeit('func_1(test_lst)', globals=globals(), number=10000))
print(timeit('func_2(test_lst)', globals=globals(), number=10000))

"""
Вывод: list comprehension работает быстрее чем традиционный итератор, 
т.к. в случае с итератором сначала создаем пустой список, на каждой итерации проверяем условие, 
и добавляем по очереди значения в новый список.
"""
