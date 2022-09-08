"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit

def make_lst(m):
    return [randint(-100, 100) for i in range(2*m+1)]


def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return seq

# data = [22, 7, 2, -5, 8, 4,9]
# shell(data)
# print(data)
# #data  # [-5, 2, 4, 7, 8, 22]

print(timeit("shell(make_lst(10))", globals=globals(), number=100))
print(timeit("shell(make_lst(100))", globals=globals(), number=100))
print(timeit("shell(make_lst(1000))", globals=globals(), number=100))

a=shell(make_lst(10))
print(f'медиана:{a[int((len(a)-1)/2)]}')

