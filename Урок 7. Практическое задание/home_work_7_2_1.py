from random import randint
from timeit import timeit


# Сортировка списка методом gnome_sort
def gnome_sort(sort_list):
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list


# Определение медианы из отсортированного массива
def median(lst):
    return orig_list[m]


m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(orig_list)
print(gnome_sort(orig_list))
print(f'Медиана = {median(gnome_sort(orig_list))}')
print(
    timeit(
        "median(gnome_sort(orig_list))",
        globals=globals(),
        number=100))

m = 100
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(f'Медиана = {median(gnome_sort(orig_list))}')
print(
    timeit(
        "median(gnome_sort(orig_list))",
        globals=globals(),
        number=100))

m = 1000
orig_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(f'Медиана = {median(gnome_sort(orig_list))}')
print(
    timeit(
        "median(gnome_sort(orig_list))",
        globals=globals(),
        number=100))

'''
[46, 1, 75, 3, 64, 46, 36, 92, 68, 18, 6, 63, 75, 92, 52, 37, 1, 32, 35, 33, 6]
[1, 1, 3, 6, 6, 18, 32, 33, 35, 36, 37, 46, 46, 52, 63, 64, 68, 75, 75, 92, 92]
Медиана = 37
0.0005184899999999965
Медиана = 53
0.005139120000000004
Медиана = 51
0.056205618999999984

'''
