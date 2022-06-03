"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randrange
from timeit import timeit

def array_median():
    for item in arr:
        n_more, n_less, n_equ = 0, 0, 0
        for item2 in arr:
            if item2 > item:
                n_more += 1
            elif item2 < item:
                n_less += 1
            else:
                n_equ += 1
        if (n_more == n_less) or (abs(n_more - n_less) < n_equ):
            return item

arr = []
m = 5
for i in range(2*m + 1):
    arr.append(randrange(100))
print(arr)    
print(array_median())    

for m in 5, 50, 500:
    arr = []
    for i in range(2*m + 1):
        arr.append(randrange(100))
    func_name = 'array_median()'
    print(f'Размер массива: {len(arr)}, {func_name} время: {timeit(func_name, globals=globals(), number=100)}')
    
'''
Размер массива: 11, array_median() время: 0.001630395999995926
Размер массива: 101, array_median() время: 0.008466950000070028
Размер массива: 1001, array_median() время: 0.10811471699992126
'''    