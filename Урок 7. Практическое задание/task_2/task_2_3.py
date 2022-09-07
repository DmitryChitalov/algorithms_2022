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

m = 10
orig_list_10 = [randint(-100, 100) for _ in range(2*m+1)]
m = 100
orig_list_100 = [randint(-100, 100) for _ in range(2*m+1)]
m = 1000
orig_list_1000 = [randint(-100, 100) for _ in range(2*m+1)]
print('Замеры statistics')

# замеры 10
print(
    timeit(
        "statistics.median(orig_list_10[:])",
        globals=globals(),
        number=1000))


# замеры 100
print(
    timeit(
        "statistics.median(orig_list_100[:])",
        globals=globals(),
        number=1000))


# замеры 1000
print(
    timeit(
        "statistics.median(orig_list_1000[:])",
        globals=globals(),
        number=1000))

print('Замеры numpy')

# замеры 10
print(
    timeit(
        "median(orig_list_10[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "median(orig_list_100[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "median(orig_list_1000[:])",
        globals=globals(),
        number=1000))


"""
ИТОГИ
Поиск медианы с сортировкой списка методом кучи
0.25552693999998155
2.2669138229994132
30.884409926000444
Поиск медианы без сортировки списка
0.022013129000697518
1.7148088540016033
80.48186990999966
Поиск медианы функцией библиотеки statistics
0.0020644559990614653
0.03314585400039505
0.5624510300003749
Поиск медианы функцией библиотеки numpy
0.10075170999880356
0.17874589199891489
0.5718858239997644

Анализ поиска медианы небольших списков 
Наиболле эффективными методами является функция стандартной библиотеки statistics либо отказ от сортировки  
На средних и больших списках наиболее эффективны библиотеки statistics и numpy
Предполагаю, что на очень больших значениях эффективнее всего numpy
"""