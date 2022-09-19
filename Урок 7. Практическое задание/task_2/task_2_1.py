from random import randint
from timeit import timeit


# Гномья сортировка
def gnome_sort(lst_obj, m):
    i = 0
    while i < len(lst_obj):
        if i == 0:
            i += 1
        if lst_obj[i] >= lst_obj[i - 1]:
            i += 1
        else:
            lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
            i -= 1
    return f'Список: {lst_obj}. Медиана: {lst_obj[m]}'


mes = int(input('Введите число: '))
N = 2*mes + 1
orig_list = [randint(-100, 100) for _ in range(2*mes + 1)]
print(gnome_sort(orig_list, mes))

print(timeit("gnome_sort(orig_list, mes)", globals=globals(), number=100))

"""
10 элементов:
Список: [-97, -87, -71, -71, -60, -58, -55, -36, -33, -24, -1, 8, 30, 30, 45, 56, 59, 62, 85, 97, 100]. Медиана: -1
0.0008367999689653516
100 элементов:
0.0038149000611156225
1000 элементов:
0.06142320006620139
"""