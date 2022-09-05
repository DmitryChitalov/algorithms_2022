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
from timeit import timeit
from random import randint

def get_mediana(my_list, m):
    for i in range(m):
        my_list.remove(max(my_list))
    return my_list

m = 10
my_list_10 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(my_list_10[:], m)", globals=globals(), number=1000))

m = 100
my_list_100 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(my_list_100[:], m)", globals=globals(), number=1000))

m = 1000
my_list_1000 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(my_list_1000[:], m)", globals=globals(), number=30))
# Результаты
# 0.0198922
# 1.2371535
# 3.0462731000000005
