from random import randint
from timeit import timeit


# Я использовала гномью сортировку
def gnome_sort(lst):
    index = 1
    i = 0
    while i < len - 1:
        if lst[i] <= lst[i + 1]:
            i, index = index, index + 1
        else:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1

    return lst[m]


m = int(input("Введите любое натуральное число: "))
len = 2 * m + 1
lst = [randint(0, 10) for _ in range(len)]
print(timeit("gnome_sort(lst)", globals=globals(), number=1000))

lst1 = [randint(0, 100) for _ in range(len)]
print(timeit("gnome_sort(lst1)", globals=globals(), number=1000))

lst2 = [randint(0, 1000) for _ in range(len)]
print(timeit("gnome_sort(lst2)", globals=globals(), number=1000))
