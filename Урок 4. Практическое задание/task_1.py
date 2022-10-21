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
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


lst = [6, 2, 3, 4]

print(func_1(lst))
print(func_2(lst))

print(timeit("func_1(lst)", globals=globals(), number=10000))
print(timeit("func_2(lst)", globals=globals(), number=10000))


'''
Вывод: Попробывал через генераторное выражение, ускорить получилось, но есть ньюанс, 
выводит числа а не индексы, пробовал через nums.index(i) скорость падает.
'''