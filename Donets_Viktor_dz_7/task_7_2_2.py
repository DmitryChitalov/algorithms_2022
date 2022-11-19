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


def no_sort(lst_obj, q):
    for i in range(q):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)


m = int(input('Введите натуральное число: '))
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(orig_list)
print(f'Медиана массива равна: {no_sort(orig_list, m)}')

# при 10 значениях
m = 10
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(
    timeit(
          "no_sort(orig_list[:], m)",
          globals=globals(),
          number=1000))
# при 100
m = 100
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(
    timeit(
          "no_sort(orig_list[:], m)",
          globals=globals(),
          number=1000))
# при 1000
m = 1000
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(
    timeit(
          "no_sort(orig_list[:], m)",
          globals=globals(),
          number=1000))

"""
Введите натуральное число: 15
[434, 679, 359, 663, 387, 38, 871, 239, 458, 299, 394, 993, 814, 519, 864, 394,
 634, 350, 439, 797, 892, 597, 803, 606, 489, 487, 308, 287, 249, 965, 988]
Медиана массива равна: 489
0.0054751999996369705
0.26629379999940284
23.925619600002392
"""
