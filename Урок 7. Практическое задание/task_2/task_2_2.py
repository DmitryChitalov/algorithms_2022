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
from random import randrange
from timeit import timeit


def median(array):
    temp_array = array[:]
    i = (len(temp_array) - 1) / 2
    while len(temp_array) > i + 1:
        temp_array.remove(max(temp_array))
    return max(temp_array)


m = int(input('Введите m (от 0 до 9):'))

arr = [randrange(100) for x in range(2 * m + 1)]

print(arr)
print('Медиана', median(arr))

print('10: ', timeit('median([randrange(100) for x in range(10)])', globals=globals(), number=100))
# 0.0009793000062927604
print('100: ', timeit('median([randrange(100) for x in range(100)])', globals=globals(), number=100))
# 0.014492499991320074
print('1000: ', timeit('median([randrange(100) for x in range(1000)])', globals=globals(), number=100))
# 0.8058652000036091
