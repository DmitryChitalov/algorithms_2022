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

mycode = '''
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
            print(new_arr)
    return new_arr
'''

print(timeit.timeit(setup='', stmt=mycode, number=10000))

mycode1 = '''
def func_1(nums):
    new_arr = []
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr
'''

print(timeit.timeit(setup='', stmt=mycode1, number=10000))

"""
При использовании List compr есть небольшой прирост скорости
"""
