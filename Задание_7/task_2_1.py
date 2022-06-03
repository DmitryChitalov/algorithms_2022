"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла, Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randrange
from heapq import heappop, heappush
from timeit import timeit

def heap_sort_median():
    heap = []
    for item in arr:
        heappush(heap, item)

    arr_ordered = []
    while heap:
        arr_ordered.append(heappop(heap))

    return arr_ordered[len(arr)//2]

arr = []
m = 5
for i in range(2*m + 1):
    arr.append(randrange(100))
print(arr)    
print(heap_sort_median())    

for m in 5, 50, 500:
    arr = []
    for i in range(2*m + 1):
        arr.append(randrange(100))
    func_name = 'heap_sort_median()'
    print(f'Размер массива: {len(arr)}, {func_name} время: {timeit(func_name, globals=globals(), number=100)}')
    
'''
Размер массива: 11, heap_sort_median() время: 0.000895002000106615
Размер массива: 101, heap_sort_median() время: 0.009417158998985542
Размер массива: 1001, heap_sort_median() время: 0.06287873399924138
'''    