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
from timeit import timeit


def bubble1(data):
    n = len(data) - 1
    for i in range(n):
        for j in range(n - i):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def bubble2(data):
    n = len(data) - 1
    for i in range(n):
        fl = False
        for j in range(n - i):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                fl = True
        if not fl:
            break
    return data


a, b = 0, 1000
s = 100
data = [randint(a, b) for _ in range(s)]

print(timeit('bubble1(data[:])', globals=globals(), number=100))
print(timeit('bubble2(data[:])', globals=globals(), number=100))
print(timeit('bubble2(data)', globals=globals(), number=100))

# 0.05075719999149442
# 0.04913460003444925
# 0.0009385999874211848
''' Доработка помогает при полной или частичной сортировке исходного массиве'''
