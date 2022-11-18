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

m = int(input('Длина массива будет равна 2m+1, введите m: '))
arr = [randint(-100, 100) for _ in range(2*m+1)]
print(f'Список: {arr}')


def median_without_sorting(arry):
    for i in range(len(arry)//2):
        i = max(arry)
        arry.remove(i)
    return f'Его медиана: {max(arry)}'


print(median_without_sorting(arr))

m = 10
arr_10 = [randint(-100, 100) for _ in range(2*m+1)]
print(f'\n10 элементов: {timeit("median_without_sorting(arr_10[:])",globals=globals(),number=1000)}')

m = 100
arr_100 = [randint(-100, 100) for _ in range(2*m+1)]
print(f'100 элементов: {timeit("median_without_sorting(arr_100[:])",globals=globals(),number=1000)}')

m = 1000
arr_1000 = [randint(-100, 100) for _ in range(2*m+1)]
print(f'1000 элементов: {timeit("median_without_sorting(arr_1000[:])",globals=globals(),number=1000)}')

"""
10 элементов: 0.0061902000000000346
100 элементов: 0.24560000000000004
1000 элементов: 24.455953800000003
"""
