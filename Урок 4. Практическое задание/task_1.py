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


n = [8, 9, 5, 7, 8, 3, 6, 6, 7, 8]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(func_1(n))
print(timeit("func_1(n)", globals=globals()))

#################################################

new_arr = []


def func_4(nums, step=0):
    if len(nums) == 0:
        return new_arr
    r = nums.pop(0)
    if r % 2 == 0:
        new_arr.append(step)
    step += 1
    return func_4(nums, step)


print(func_4(n))
print(timeit("func_4(n)", globals=globals()))


## За счет перехода к рекурсивной функции мы избавились от цикла который придавал функции сложность
# O(n) и перешли к сложности O(1), что намного быстрее, результат подтвержден замерами


