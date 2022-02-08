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

def shella(massiv):
    inc = len(massiv) // 2
    while inc:
        for i, elem in enumerate(massiv):
            while i >= inc and massiv[i - inc] > elem:
                massiv[i] = massiv[i - inc]
                i -= inc
            massiv[i] = elem
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
  
data_1 = [randint (0,2000) for i in range(0, 10+1)]
shella(data_1)
print(f'{timeit("(data_1[:])", globals=globals(), number=1000)}', data_1)

data_2 = [randint (0,2000) for z in range(0, 100+1)]
shella(data_2)
print(f'{timeit("(data_2[:])", globals=globals(), number=1000)}', data_2)

data_3 = [randint (0,2000) for q in range(0, 1000+1)]
shella(data_3)
print(f'{timeit("(data_3[:])", globals=globals(), number=1000)}', data_3)

"""
сортировка Шелла:
при 10    - 0.00014670006930828094
при 100   - 0.0005620999727398157
при 1000  - 0.002624700078740716
"""

