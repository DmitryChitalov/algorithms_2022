from random import randint
from timeit import timeit


def median_not_sort(lst, m):
    while m > 0:
        lst.pop(lst.index(max(lst)))
        m -= 1
    return lst.pop(lst.index(max(lst)))


mes = int(input('Введите число: '))
N = 2*mes + 1
orig_list = [randint(-100, 100) for _ in range(N)]

print(median_not_sort(orig_list[:], mes))
print(timeit("median_not_sort(orig_list[:], mes)", globals=globals(), number=100))

