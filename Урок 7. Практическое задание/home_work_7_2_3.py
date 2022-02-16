from random import randint
from timeit import timeit
from statistics import median


def gnome_median(orig_list):
    return median(orig_list[:])


m = 10
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(orig_list)
print(gnome_median(orig_list))
print(
    timeit(
        "gnome_median(orig_list[:])",
        globals=globals(),
        number=100))

m = 100
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(gnome_median(orig_list))
print(
    timeit(
        "gnome_median(orig_list[:])",
        globals=globals(),
        number=100))

m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(gnome_median(orig_list))
print(
    timeit(
        "gnome_median(orig_list[:])",
        globals=globals(),
        number=100))

'''
[23, 97, 83, 55, 17, 41, 9, 47, 29, 51, 42, 21, 66, 52, 71, 17, 77, 6, 40, 25, 74]
42
0.0001572580000000004
52
0.0013222530000000024
51
0.03080077099999999

В первом варианте 7_2_1 наверно посчитала не то время.
Поэтому сравнивать буду 2-ой и 3-ий варианты (7_2_2 и 7-3_3).
Встроенная функция median дает самые быстрые результаты.
'''
