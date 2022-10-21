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
    return [i for i, e in enumerate(nums) if e % 2 == 0]


lst = list(range(100))

print(timeit("func_1(lst)", globals=globals()))
print(timeit("func_2(lst)", globals=globals()))


# использовал list comprehension вместо цикла
# это уменьшило время выполнения, т.к. lc работает быстрее чем цикл
