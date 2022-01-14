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


def get_mediana(arr, m):
    for i in range(m):
        arr.remove(max(arr))
    return max(arr)


m = 10
arr_10 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(arr_10[:], m)", globals=globals(), number=1000))

m = 100
arr_100 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(arr_100[:], m)", globals=globals(), number=1000))

m = 1000
arr_1000 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(arr_1000[:], m)", globals=globals(), number=30))


"""
Результаты:
            m = 10 - 0.01849009999999998
            m = 100 - 1.0415120999999998
            m = 1000 - 3.0872741
"""