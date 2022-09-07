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
import statistics
from random import randint
from timeit import timeit
from numpy import median


m = 10
orig_list = [randint(-100, 100) for _ in range(2*m+1)]
print(f'Исходный список: {orig_list}')
print(f'Отсортированная копия для проверки: {sorted(orig_list[:])}')
print(f'Медиана = {statistics.median(orig_list)}')
print(f'Медиана = {int(median(orig_list))}')


print('Замеры statistics')

# замеры 10
print(
    timeit(
        "statistics.median(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "statistics.median(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "statistics.median(orig_list)",
        globals=globals(),
        number=1000))

print('Замеры numpy')

# замеры 10
print(
    timeit(
        "median(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "median(orig_list)",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "median(orig_list)",
        globals=globals(),
        number=1000))


"""
ИТОГИ
Поиск медианы с сортировкой списка методом кучи
0.1414635970004383
0.7642583890001333
10.474215252999784
Поиск медианы без сортировки списка
0.017381194999870786
0.3872662739995576
25.51902260099996
Поиск медианы функцией библиотеки statistics
0.006574248999640986
0.07222399300007964
0.26326558900018426
Поиск медианы функцией библиотеки numpy
0.34361335700032214
0.10602535599991825
0.3065561670000534

Анализ поиска медианы небольших списков 
Наиболле эффективными методами является функция стандартной библиотеки statistics либо отказ от сортировки  
На средних и больших списках наиболее эффективны библиотеки statistics и numpy
"""