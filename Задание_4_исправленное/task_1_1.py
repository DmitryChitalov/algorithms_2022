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
    new_arr = [item for item in nums if item % 2 == 0]
    return new_arr

def exec(func, cnt):
    func(list(range(cnt)))

cnt = 1
for n in range(1, 4):
    print(f'func_1: cnt = {cnt}, время = {timeit("exec(func_1, cnt)", globals=globals())}')
    print(f'func_2: cnt = {cnt}, время = {timeit("exec(func_2, cnt)", globals=globals())}')
    cnt *= 4

# В func_2 цикл заменен на фильтр списка, скорость возросла
# На уровне Питона в срезе цикла нет, я имел ввиду реализацию среза на C - там же цикл используется, иначе никак
