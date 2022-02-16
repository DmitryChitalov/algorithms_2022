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

m = int(input('Длина массива будет равна 2m+1, введите m: '))
arr = [randint(-100, 100) for _ in range(2*m+1)]


def shellsort(a):
    def new_increment(aa):
        v = int(len(aa) / 2)
        yield v
        while v != 1:
            if v == 2:
                v = 1
            else:
                v = int(round(v / 2.2))
            yield v

    for increment in new_increment(a):
        for i in range(increment, len(a)):
            for j in range(i, increment - 1, -increment):
                if a[j - increment] < a[j]:
                    break
                a[j], a[j - increment] = a[j - increment], a[j]
    return f'Отсортированный список: {a}, медиана: {a[m]}'


print(shellsort(arr))

m = 10
arr_10 = [randint(-100, 100) for _ in range(2*m+1)]
print(f'\n10 элементов: {timeit("shellsort(arr_10[:])",globals=globals(),number=1000)}')

m = 100
arr_100 = [randint(-100, 100) for _ in range(2*m+1)]
print(f'100 элементов: {timeit("shellsort(arr_100[:])",globals=globals(),number=1000)}')

m = 1000
arr_1000 = [randint(-100, 100) for _ in range(2*m+1)]
print(f'1000 элементов: {timeit("shellsort(arr_1000[:])",globals=globals(),number=1000)}')

"""
10 элементов: 0.025227199999999783
100 элементов: 0.41223300000000007
1000 элементов: 9.7640614
"""
