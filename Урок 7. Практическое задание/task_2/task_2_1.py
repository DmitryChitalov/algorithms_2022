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
import random
import timeit


def random_mass(num: int):
    mas = []
    for i in range(num * 2 + 1):
        mas.append(int(random.uniform(-100, 100)))
    return mas


def gnom_sort(mass):
    i, size = 1, len(mass)
    while i < size:
        if mass[i - 1] <= mass[i]:
            i += 1
        else:
            mass[i - 1], mass[i] = mass[i], mass[i - 1]
            if i > 1:
                i -= 1
    return mass


i = 10
mas = gnom_sort(random_mass(i))
per = """
mas = gnom_sort(random_mass(i))
"""
print(mas)
print("Медиана = ", mas[i + 1], " Элемент ", i + 1)
print(timeit.timeit(setup='', stmt=per, number=10000, globals=globals()))

i = 100
mas = gnom_sort(random_mass(i))
per = """
mas = gnom_sort(random_mass(i))
"""
print(mas)
print("Медиана = ", mas[i + 1], " Элемент ", i + 1)
print(timeit.timeit(setup='', stmt=per, number=10000, globals=globals()))

i = 1000
mas = gnom_sort(random_mass(i))
per = """
mas = gnom_sort(random_mass(i))
"""
print(mas)
print("Медиана = ", mas[i + 1], " Элемент ", i + 1)
print(timeit.timeit(setup='', stmt=per, number=100, globals=globals()))
