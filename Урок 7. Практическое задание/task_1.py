from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i+1] > lst_obj[i]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]


def bubble_sort_2(lst_obj):
    n = 1
    flag = True
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i + 1] > lst_obj[i]:
                flag = False
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if flag:
            return lst_obj
        n += 1
    return lst_obj


print(bubble_sort(orig_list[:]))
print(bubble_sort_2(orig_list[:]))
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_2(orig_list[:])", globals=globals(), number=1000))
"""
[90, 83, 72, 9, 5, -19, -39, -57, -69, -87]
[90, 83, 72, 9, 5, -19, -39, -57, -69, -87]
0.008534900029189885
0.010120199993252754
Разницы между скоростью работы алгоритмов практически нет. Улучшеный алгоритм будет быстрее, если туда сразу передать
отсортированный список, потому что он не будет делать ненужные итерации по списку как первый.
"""