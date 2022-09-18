"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
import random
import statistics
import timeit


def random_mass(num: int):
    mas = []
    for i in range(num * 2 + 1):
        mas.append(int(random.uniform(-100, 100)))
    return mas


i = 10
mass = random_mass(i)
med = statistics.median(mass)
per = """
mass = random_mass(i)
med = statistics.median(mass)
"""
print("Массив ", mass)
print("Медиана ", med)
print(timeit.timeit(setup='', stmt=per, number=10000, globals=globals()))

i = 100
mass = random_mass(i)
med = statistics.median(mass)
per = """
mass = random_mass(i)
med = statistics.median(mass)
"""
print("Массив ", mass)
print("Медиана ", med)
print(timeit.timeit(setup='', stmt=per, number=10000, globals=globals()))

i = 1000
mass = random_mass(i)
med = statistics.median(mass)
per = """
mass = random_mass(i)
med = statistics.median(mass)
"""
print("Массив ", mass)
print("Медиана ", med)
print(timeit.timeit(setup='', stmt=per, number=100, globals=globals()))

"""
Из трех вариантов самое быстродейственный являетя встроенные в python. Так как он более оптимизированный.
В первом варианте очень много времени занимает гномья сортировка, а тором методе идет поиск в несортированном массиве и 
идет перебор очень большого колества данных
"""
