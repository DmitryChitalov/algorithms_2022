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


def shell(num):
    n = len(num) // 2
    while n:
        for i, j in enumerate(num):
            while i >= n and num[i - n] > j:
                num[i] = num[i - n]
                i -= n
            num[i] = j
        n = 1 if n == 2 else int(n * 5.0 / 11)
    return num


print('----10----')
m = 10
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(lst)
print(timeit("shell(lst[:])[m]", globals=globals(), number=1000))
print(shell(lst))
print(shell(lst)[m])

print('----100----')
m = 100
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(lst)
print(timeit("shell(lst[:])[m]", globals=globals(), number=1000))
print(shell(lst))
print(shell(lst)[m])

print('----1000----')
m = 1000
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(lst)
print(timeit("shell(lst[:])[m]", globals=globals(), number=1000))
print(shell(lst))
print(shell(lst)[m])

"""
----10----
0.043285200000000024

----100----
0.9177111

----1000----
13.7568424
"""
