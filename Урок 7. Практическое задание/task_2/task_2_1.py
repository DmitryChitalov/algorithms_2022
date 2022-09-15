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
from collections import Counter
from timeit import timeit


def count_sort(arr):
    """
    Сортирует массив по возрастанию. Довольно эффективен когда область определения достаточно мала по сравнению с
    сортируемым массивом, например, миллион натуральных чисел меньших 1000.
    """
    counter = Counter(arr)
    arr.clear()
    for i in range(min(counter), max(counter) + 1):
        arr.extend([i] * counter[i])


m = int(input('Введите m: '))
ARRAY = [randint(-m, m) for _ in range(2 * m + 1)]
print('Создан массив длинной 2m + 1:', ARRAY)
array = ARRAY[:]
count_sort(array)
print('Отсортированный массив:', array)

print()
print('Отсортирован:', ARRAY == sorted(ARRAY[:]))
print(f'Время сортировки массива длиной {len(ARRAY)}:', timeit('count_sort(ARRAY[:])', globals=globals(), number=1000))
print('Медиана массива', array[m])

print()
print('Отсортирован:', ARRAY == sorted(ARRAY[:]))
ARRAY *= 9
array = ARRAY[:]
count_sort(array)
m = (len(array) - 1) // 2
print(f'Время сортировки массива длиной {len(ARRAY)}:', timeit('count_sort(ARRAY[:])', globals=globals(), number=1000))
print('Медиана массива', array[m])

print()
print('Отсортирован:', ARRAY == sorted(ARRAY[:]))
ARRAY *= 11
array = ARRAY[:]
count_sort(array)
m = (len(array) - 1) // 2
print(f'Время сортировки массива длиной {len(ARRAY)}:', timeit('count_sort(ARRAY[:])', globals=globals(), number=1000))
print('Медиана массива', array[m])


print()
print('Отсортирован:', ARRAY == sorted(ARRAY[:]))
array = ARRAY[:]
array.sort()
m = (len(array) - 1) // 2
print(f'Время сортировки массива длиной {len(ARRAY)}:', timeit('ARRAY[:].sort()', globals=globals(), number=1000))
print('Медиана массива', array[m])

"""
Введите m: 5
Создан массив длинной 2m + 1: [1, -3, 2, 2, 2, -1, 1, -1, 5, 4, -5]
Отсортированный массив: [-5, -3, -1, -1, 1, 1, 2, 2, 2, 4, 5]

Отсортирован: False
Время сортировки массива длиной 11: 0.0066127899999628426
Медиана массива 1

Отсортирован: False
Время сортировки массива длиной 99: 0.01220138799999404
Медиана массива 1

Отсортирован: False
Время сортировки массива длиной 1089: 0.0709094339999865
Медиана массива 1

Отсортирован: False
Время сортировки массива длиной 1089: 0.06309288299962645
Медиана массива 1
"""
