"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from memory_profiler import profile
from time import time


def timer1(func):
    def time_mes(*args, **kwargs):
        start = time()
        act = func(*args, **kwargs)
        stop = time()
        res = stop - start
        print(f'Функция выполняется за {res} c')
        return act
    return time_mes


def gen_int(n):
    a = [randint(0, 10000) for _ in range(n)]
    return a


# @profile
@timer1
def bubble_smart(m):
    fl = False
    i = 1
    while i < len(m):
        for j in range(len(m)-i):
            if m[j] < m[j+1]:
                fl = True
                m[j], m[j+1] = m[j+1], m[j]
        if fl is False:
            break
        i += 1
    return m

# @profile
@timer1
def bubble_2(m):
    i = 1
    while i < len(m):
        for j in range(len(m)-i):
            if m[j] < m[j+1]:
                fl = True
                m[j], m[j+1] = m[j+1], m[j]
        i += 1
    return m


arr = gen_int(1000)
arr2 = sorted(arr, reverse=True)
print('"Умная" сортировка случайного массива')
bubble_smart(arr[:])
print('"Умная" сортировка упорядоченного массива')
bubble_smart(arr2[:])
print('Обычная сортировка упорядоченного массива')
bubble_2(arr2[:])

"""Умная сортировка дает значительный выигрыш если на входе уже отсортированный массив"""