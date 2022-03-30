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
from timeit import timeit
from random import randint


def without_sort(lst):
    temp = lst
    for i in range(len(lst) // 2):
        temp.remove(max(temp))
    return max(temp)


m = int(input("Введите m: "))
lst_obj = [randint(0, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив: \n{lst_obj}\n')
print(without_sort(lst_obj))


print(timeit("without_sort(lst_obj[:])", globals=globals(), number=1000))

"""
m = 10
0.002380300000368152

m = 100
0.07894809999925201

m = 1000
6.859817700000349
"""