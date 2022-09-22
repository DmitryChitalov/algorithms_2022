from random import randint
from timeit import timeit
from statistics import median


mes = int(input('Введите число: '))
orig_list = [randint(-1000, 1000) for _ in range(2*mes + 1)]

print(timeit("median(orig_list)", globals=globals(), number=1000))
"""
10:
0.0005986000178381801
100:
0.0064721000380814075
1000:
0.18483369995374233
Разница на средних и маленьких массивах разница почти не видна, но на больших массивах быстрее работает гномья
и медлненнее всего метод без сортировки.
"""