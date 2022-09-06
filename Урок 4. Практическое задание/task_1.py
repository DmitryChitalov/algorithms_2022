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


other_nums = [x for x in range(10**3)]

print(func_1(other_nums))
print(timeit('func_1(other_nums)', globals=globals(), number=10000))


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]

    return new_arr


print(func_2(other_nums))
print(timeit('func_2(other_nums)', globals=globals(), number=10000))

"""
В задании, мной была добавлена новая функция func_2().
Данная функция выполняет требуемое от нее задание быстрее, т.к формирование нового списка выполняется с помошью list comprehensions, а не метода append, что подтверждают замеры, сделанные с помошью модуля timeit
"""