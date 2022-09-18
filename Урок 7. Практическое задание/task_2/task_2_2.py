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
from collections import Counter
import random
import timeit


def random_mass(num: int):
    mas = []
    for i in range(num * 2 + 1):
        mas.append(int(random.uniform(-100, 100)))
    return mas


def my_mode(mass):
    c = Counter(mass)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


i = 10
mas = my_mode(random_mass(i))
print("Медиана равна", mas)
per = """
mas = my_mode(random_mass(i))
"""
print(timeit.timeit(setup='', stmt=per, number=10000, globals=globals()))

i = 100
mas = my_mode(random_mass(i))
print("Медиана равна", mas)
per = """
mas = my_mode(random_mass(i))
"""
print(timeit.timeit(setup='', stmt=per, number=10000, globals=globals()))

i = 1000
mas = my_mode(random_mass(i))
print("Медиана равна", mas)
per = """
mas = my_mode(random_mass(i))
"""
print(timeit.timeit(setup='', stmt=per, number=100, globals=globals()))
