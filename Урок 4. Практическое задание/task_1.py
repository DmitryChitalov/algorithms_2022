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

random_nums = [x for x in range(10**3)]

print(func_1(random_nums))
print(timeit('func_1(random_nums)', globals=globals(), number=10000))

def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

print(func_2(random_nums))
print(timeit('func_2(random_nums)', globals=globals(), number=10000))

# вторая функция выполняет требования задания быстрее, чем первоначальная так list comprehensions формирует список быстрее чем метод append
# замеры с помощью модуля timeit показали, что время исполнения второй функции быстрее
