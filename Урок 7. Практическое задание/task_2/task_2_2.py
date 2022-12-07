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


def median(m):
    arr = [randint(0, m) for i in range(2 * m + 1)]
    count = 0
    arr_copy = arr[:]
    while count < m:
        arr_copy.remove(max(arr_copy))
        count += 1
    return arr, max(arr_copy)


print(timeit('median(5)', globals=globals(), number=1000))
print(timeit('median(50)', globals=globals(), number=1000))
print(timeit('median(500)', globals=globals(), number=1000))

"""
Результат:
0.00813430012203753
0.1135468001011759
5.318581199971959
"""
