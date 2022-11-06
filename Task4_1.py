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


print(func_1(nums))
print(timeit('func_1(nums)', globals=globals(), number=100000))


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


'''при решении с ипользованием list comprehension скорость выполнения кода выросла так-как для этого его и придумали
плюс код стал более лаконичным'''

print(func_2(nums))
print(timeit('func_2(nums)', globals=globals(), number=100000))