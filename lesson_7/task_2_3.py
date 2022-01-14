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
from timeit import timeit
from random import randrange
from statistics import median


def find_median(m):
    lst = [randrange(-100, 100) for _ in range(2 * m + 1)]
    lst_median = median(lst)
    return lst, lst_median


print(find_median(2))

print(timeit('find_median(10)', globals=globals(), number=1000))  # 0.021418700000000006
print(timeit('find_median(100)', globals=globals(), number=1000))  # 0.10643330000000001
print(timeit('find_median(1000)', globals=globals(), number=1000))  # 1.0924332

"""При малом количестве элементов в массиве (10 элементов) все три способа оказались приблизительно одинаково 
эффективными. Однако, при увеличении количества чисел в массиве, самым эффективным в плане скорости выполнения 
оказался третий способ - решение задачи с помощью встроенной функции поиска медианы. Самым медленным оказалось 
решение задачи с помощью гномьей сортировки."""
