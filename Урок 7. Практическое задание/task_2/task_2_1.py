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


def shellsort(lst_obj):
    def new_increment(array):
        i = int(len(array) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(round(i/2.2))
            yield i
    for increment in new_increment(lst_obj):
        for i in range(increment, len(lst_obj)):
            for j in range(i, increment - 1, -increment):
                if lst_obj[j - increment] < lst_obj[j]:
                    break
                lst_obj[j], lst_obj[j - increment] = lst_obj[j - increment], lst_obj[j]
    return lst_obj


arr_10 = []
for _ in range(11):
    arr_10.append(randint(1, 10))
shellsort(arr_10)
s1 = """
shellsort(arr_10)
median(arr_10)
"""

arr_100 = []
for _ in range(101):
    arr_100.append(randint(1, 100))
shellsort(arr_100)
s2 = """
shellsort(arr_100)
median(arr_100)"""

arr_1000 = []
for _ in range(1001):
    arr_1000.append(randint(1, 100))
shellsort(arr_1000)
s3 = """
shellsort(arr_1000)
median(arr_1000)"""

print(arr_10)
print(arr_100)
print(arr_1000)


def median(lst_obj):
    m = (len(lst_obj) - 1) // 2
    return lst_obj[m]

print(f'med:{(median(arr_10))}')
print(f'med:{(median(arr_100))}')
print(f'med:{(median(arr_1000))}')

print(timeit(s1, globals=globals(), number=1000), 's1')
print(timeit(s2, globals=globals(), number=1000), 's2')
print(timeit(s3, globals=globals(), number=1000), 's3')




