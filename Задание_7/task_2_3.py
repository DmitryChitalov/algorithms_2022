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

from random import randrange
from timeit import timeit
from statistics import median

def statistics_median():
    return median(arr)

arr = []
m = 5
for i in range(2*m + 1):
    arr.append(randrange(100))
print(arr)    
print(statistics_median())    

for m in 5, 50, 500:
    arr = []
    for i in range(2*m + 1):
        arr.append(randrange(100))
    func_name = 'statistics_median()'
    print(f'Размер массива: {len(arr)}, {func_name} время: {timeit(func_name, globals=globals(), number=100)}')
    
'''
Размер массива: 11, statistics_median() время: 0.00017340900012641214
Размер массива: 101, statistics_median() время: 0.0008751829991524573
Размер массива: 1001, statistics_median() время: 0.018952517999423435

На случайном массиве быстрее всех работает встроенная функция stsistics.median
'''    
