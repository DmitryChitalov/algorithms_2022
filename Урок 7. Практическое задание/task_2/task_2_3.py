"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""


from statistics import median
from random import randrange
from timeit import timeit

m = int(input('Введите m:'))

arr = [randrange(100) for x in range(2 * m + 1)]

print(arr)
print(sorted(arr))
print('Медиана - ', median(arr))

print('10: ', timeit('median([randrange(100) for x in range(10)])', globals=globals(), number=100))
print('100: ', timeit('median([randrange(100) for x in range(10)])', globals=globals(), number=100))
print('1000: ', timeit('median([randrange(100) for x in range(10)])', globals=globals(), number=100))

"""
10:  0.0006886001210659742
100:  0.0006688002031296492
1000:  0.0006842000875622034
"""

"""
Выводы:
Сортировка:
10:  0.0016391000244766474
100:  0.09056790010072291
1000:  9.537067199824378
Без сортировки:
10:  0.0009676001500338316
100:  0.014778999844565988
1000:  0.6453964000102133
Встроенной функцией:
10:  0.0006886001210659742
100:  0.0006688002031296492
1000:  0.0006842000875622034
Вариант с предварительной сортировкой самый медленный и результаты ухудшаются при увеличении эллементов. Вариант без 
сортировки чуть лучше. И, как и предполагалось, встроенная функция работает одинаково быстро на маленьких и больших массивах.
"""