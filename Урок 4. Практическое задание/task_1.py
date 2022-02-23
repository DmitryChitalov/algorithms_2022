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


nums = [i for i in range(10000)]
func_1(nums)
func_2(nums)
print(f'Время выполнения функции func_1 = {timeit("func_1(nums)", globals=globals(), number=1000)}')

print(f'Время выполнения функции func_2 = {timeit("func_2(nums)", globals=globals(), number=1000)}')

# Время выполнения функции func_1 = 0.7421426
# Время выполнения функции func_2 = 0.5928495999999999
# Используя "list comprehension" удалось немного увеличить скорость обработки функции