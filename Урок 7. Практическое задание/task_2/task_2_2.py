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


from random import randint
from timeit import timeit


def get_mediana(obj_list):

    temp = obj_list
    for i in range(len(obj_list) // 2):
        temp.remove(max(temp))
    return max(temp)


m = 10
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(get_mediana(obj_list[:]))
print(timeit("get_mediana(obj_list[:])", globals=globals(), number=1000))

m = 100
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(timeit("get_mediana(obj_list[:])", globals=globals(), number=1000))

m = 1000
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(timeit("get_mediana(obj_list[:])", globals=globals(), number=1000))


"""
10 элементов - 0.007780406000165385
100 элементов - 0.2441539700002977
1000 элементов - 21.529072313999677
"""