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


def func_median(lst):
    ln = len(lst) // 2 + 1
    while len(lst) > ln:
        lst.remove(max(lst))
    return max(lst)


list_in = [randint(-100, 100) for _ in range(11)]

# замеры 10
print(f'10 элементов - {timeit("func_median(list_in[:])", globals=globals(), number=1000)}')
print(f'медиана = {func_median(list_in[:])}')


list_in = [randint(-100, 100) for _ in range(101)]
# замеры 100
print(f'100 элементов - {timeit("func_median(list_in[:])", globals=globals(), number=1000)}')
print(f'медиана = {func_median(list_in[:])}')


list_in = [randint(-100, 100) for _ in range(1001)]
# замеры 1000
print(f'1000 элементов - {timeit("func_median(list_in[:])", globals=globals(), number=1000)}')
print(f'медиана = {func_median(list_in[:])}')


"""
Результаты замеров

10 элементов - 0.006590900011360645
медиана = -40
100 элементов - 0.20339460001559928
медиана = 0
1000 элементов - 16.817552399996202
медиана = 4

"""