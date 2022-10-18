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


def find_median(arr):
    while len(arr) > m + 1:
        arr.remove(max(arr))
    median = max(arr)
    return median


# замер 10:  0.004657099998439662
m = 5
my_array = [randint(1, 100) for _ in range(2 * m + 1)]

print(
    timeit(
        "find_median(my_array[:])",
        globals=globals(),
        number=1000))

print('исходный массив:', my_array)
print('медиана: ', find_median(my_array[:]))

# замер 100:  0.16441050000139512
m = 50
my_array = [randint(1, 100) for _ in range(2 * m + 1)]

print(
    timeit(
        "find_median(my_array[:])",
        globals=globals(),
        number=1000))

print('исходный массив:', my_array)
print('медиана: ', find_median(my_array[:]))

# замер 1000:  13.118751000001794
m = 500
my_array = [randint(1, 100) for _ in range(2 * m + 1)]

print(
    timeit(
        "find_median(my_array[:])",
        globals=globals(),
        number=1000))

print('исходный массив:', my_array)
print('медиана: ', find_median(my_array[:]))
