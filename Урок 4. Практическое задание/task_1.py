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


nums = list(n for n in range(1000))


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


print(timeit("func_1(nums)", globals=globals(), number=1000))
print(timeit("func_2(nums)", globals=globals(), number=1000))


'''
Время работы func_1, которая использует цикл для перебора  0.07984190000000001 
Время работы func_2, которая использует List comprehension 0.0005693999999999977
List comprehension работает быстрее, так как не требуется многократного вызова append в цикле и создания нового списка
'''
