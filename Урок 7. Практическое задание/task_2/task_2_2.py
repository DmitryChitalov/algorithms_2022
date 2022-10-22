"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit

lst_10 = [randint(0, 1000) for _ in range(11)]
lst_100 = [randint(0, 1000) for _ in range(101)]
lst_1000 = [randint(0, 1000) for _ in range(1001)]


def get_mediana(lst_obj):
    for i in range(len(lst_obj) // 2):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)


print(get_mediana(lst_10))
print(get_mediana(lst_100))
print(get_mediana(lst_1000))
print(timeit("get_mediana(lst_10)", globals=globals(), number=1000))
print(timeit("get_mediana(lst_100)", globals=globals(), number=1000))
print(timeit("get_mediana(lst_1000)", globals=globals(), number=1000))