"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
import timeit

nums = [n for n in range(2, 1000, 3)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [n for n in range(len(nums)) if nums[n] % 2 == 0]
    return new_arr


s = """
new_arr = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        new_arr.append(i)"""
print(timeit.timeit(s, globals=globals(), number=100000))
print(timeit.timeit('new_arr = [n for n in range(len(nums)) if nums[n] % 2 == 0]', globals=globals(), number=100000))

# Произведён замер времени выполнения кода с помощью модуля timeit
# Общее время выполнения для funnc_1 в среднем 2.0 сек, для func_2 в среднем 1.6 сек, func_2 быстрее примерно на 20%
# Вероятно алгоритмы list comprehension более оптимизированы чем обычный цикл for
