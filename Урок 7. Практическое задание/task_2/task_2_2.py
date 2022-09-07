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


arr_10 = []
for _ in range(11):
    arr_10.append(randint(1, 10))

arr_100 = []
for _ in range(101):
    arr_100.append(randint(1, 100))

arr_1000 = []
for _ in range(1001):
    arr_1000.append(randint(1, 100))

print(arr_10)
print(arr_100)
print(arr_1000)


def unsort_med(lst_obj):
    while True:
        for elem in lst_obj:
            count = 0
            for x in lst_obj:
                if x < elem:
                    count += 1
            if count == len(lst_obj) // 2:
                return elem
        lst_obj.remove(max(lst_obj))


print(f'med:{(unsort_med(arr_10))}')
print(f'med:{(unsort_med(arr_100))}')
print(f'med:{(unsort_med(arr_1000))}')

u1 = """
unsort_med(arr_10)"""

u2 = """
unsort_med(arr_100)"""

u3 = """
unsort_med(arr_1000)"""

print(timeit(u1, globals=globals(), number=1000), 'u1')
print(timeit(u2, globals=globals(), number=1000), 'u2')
print(timeit(u3, globals=globals(), number=1000), 'u3')





