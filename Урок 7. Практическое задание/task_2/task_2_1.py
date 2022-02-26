"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
import timeit

def heapify(nums, size, main_i):  
    big = main_i
    left = (2 * main_i) + 1
    right = (2 * main_i) + 2
    if left < size and nums[left] > nums[big]:
        big = left
    if right < size and nums[right] > nums[big]:
        big = right
    if big != main_i:
        nums[main_i], nums[big] = nums[big], nums[main_i]
        heapify(nums, size, big)

def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums[int((len(li)-1)/2)]

m = 500  # индекс медианы
li = [randint(-100, 100) for i in range(2*m+1)]
print(li)
mediana = heap_sort(li[:])

res = timeit.timeit('heap_sort(li[:])', number=10, globals=globals())

print(f'mediana {li[int((len(li)-1)/2)]} index {m} в массиве длинной {len(li)} за {res} секунд')
'''
mediana 80 index 5 в массиве длинной 11 за 0.00017095100065489532 секунд

mediana -4 index 50 в массиве длинной 101 за 0.002685572000700631 секунд

mediana 98 index 500 в массиве длинной 1001 за 0.040839887000402086 секунд

'''
