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


def median_search(seq):
    new_list = seq
    for _ in range(len(orig_list) // 2):
        new_list.remove(max(new_list))
    return max(new_list)


m = 10
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана :{median_search(orig_list)}')
# замеры 10
print(
    timeit(
        "median_search(orig_list[:])",
        globals=globals(),
        number=1000))
m = 100
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана :{median_search(orig_list)}')
# замеры 100
print(
    timeit(
        "median_search(orig_list[:])",
        globals=globals(),
        number=1000))

m = 1000
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Медиана :{median_search(orig_list)}')
# замеры 1000
print(
    timeit(
        "median_search(orig_list[:])",
        globals=globals(),
        number=1000))

"""

Результаты тестов.
(m = 10)
0.0003142000059597194
(m = 100)
0.00037460000021383166
(m = 1000)
0.006531800027005374

Исходя из того, что было сказано на уроке.., вроде, правильно, удаляются максимальные элементы до m и
медианой становится максимальный из оставшихся.
Но не понятно почему медианой получаются абсолютно разные по индексам элементы...ну то есть из оставшегося списка
бывало, что и [0] или [-1] элемент попадался медианой когда принтами покрывал.

"""