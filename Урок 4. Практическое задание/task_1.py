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
from numpy import array, where


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(0, len(nums), 2)]


def func_3(nums):
    return where(array(nums) % 2 == 0)


def func_4(nums):
    return [i for i, num in enumerate(nums) if num % 2 == 0]


def func_5(nums):
    return [i for i in range(0, len(nums)) if nums[i] % 2 == 0]


NUMS = [el for el in range(1000)]

print("LC без условия проверки значения на чётность:",
      timeit(
          "func_2(NUMS[:])",
          globals=globals(),
          number=1000))
print("Используем библиотеку numpy:",
      timeit(
          "func_3(NUMS[:])",
          globals=globals(),
          number=1000))

print("LC с проверкой значения из списка на чётность:",
      timeit(
          "func_5(NUMS[:])",
          globals=globals(),
          number=1000))

print("Первоначальный пример:",
      timeit(
          "func_1(NUMS[:])",
          globals=globals(),
          number=1000))

print("Используем встроенную функцию enumerate:",
      timeit(
          "func_4(NUMS[:])",
          globals=globals(),
          number=1000))

"""
В конкретном данном случае, если нам известно, что исходный массив наполнен с помощью цикла el for el in range(10000),
то самым производительным вариантом будет func_2, используя lc и сокращение циклов,
за счёт перебора только чётных индексов мы получаем колоссальное преимущество по времени.
НО! Если в списке будет список из произвольных цифр, то алгоритм func_2 не будет выполнять поставленную задачу
из-за отсутствия условия. Если отбросить этот вариант, то func_5 - это та же функция func_2, только с условием 
на чётность. Я расположил принты замеров времени в порядке скорости их выполнения.
Лучшее время показала библиотека numpy (Функцию func_2 опустим, в силу её специфики) 
"""
