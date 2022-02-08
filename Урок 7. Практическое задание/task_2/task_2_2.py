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


import random
from timeit import timeit

massive = []
def mediana(argument):
    for i in range(len(argument)):
        less = 0
        more = 0
        for x in range(len(argument)):
            if argument[i] < argument[x]:
                less += 1
            elif argument[i] > argument[x]:
                more += 1
            elif argument[i] == argument[x]:
                less += 1
                more += 1
        if more == less:
            median = argument[i]
    return median



for i in range(1000+1):
    massive.append(random.randint(0, 2000))

print(f'массив: {massive}')
print(f'Медиана в массиве: {mediana(massive)}')
print(f'{timeit("(mediana(massive))", globals=globals(), number=1000)}')

"""
при 10 - 
массив: [1832, 1333, 385, 723, 785, 171, 1638, 1721, 375, 473, 1183]
Медиана в массиве: 785
0.024466499919071794

при 100 - 
1.3140128999948502

при 1000 -
106.94403600005899
"""
