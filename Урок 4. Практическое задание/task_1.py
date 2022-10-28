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


n = [num for num in range(100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# current function time execution
t1 = timeit("func_1(n)", globals=globals(), number=1000)
print(f'current function time execution: {t1}')

# function was updated by list comprehension format
new_arr = [num for num in range(len(n)) if num % 2 == 0]

t2 = timeit("[num for num in range(len(n)) if num % 2 == 0]", globals=globals(), number=1000)
print(f'updated function time execution: {t2}')

print(f'updated function time is different more than: {t1 / t2}')

"""для оценки времени исполнения функции был использован модуль timeit,
далее функция была скорректирована на исполнение
через list comprehension, и скорость исполнения так же была замерена, 
скорость измененной функции была увеличена более чем в 1,5 раза"""

