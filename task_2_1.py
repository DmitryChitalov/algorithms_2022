from random import randint
from timeit import timeit


def gnom_sort(res):
    n, i = len(res), 0
    while i + 1 < n:
        if res[i + 1] >= res[i]:
            i += 1
        else:
            res[i], res[i + 1] = res[i + 1], res[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    return res


m = int(input('Введите число: '))
ls = [randint(-100, 100) for _ in range(2 * m + 1)]
ls_1 = gnom_sort(ls[:])
print(f'Медиана массива: {ls_1[m]}')

print(timeit("gnom_sort(ls[:])", globals=globals(), number=1000))

'''
медиана - число с индексом m
10 элементов:   0.013466300000000153
100 элементов:  4.3420030999999994
1000 элементов: 133.0667401
'''
