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

"""
Результат выполнения:
C:\python_projects\Algoritm\lesson_7\task\Scripts\python.exe C:\python_projects\Algoritm\lesson_7\task\task_2_1.py 
Для списка - [52, -94, -97, 99, 53, -47, -32, -26, -77, 76, 73, 69, -68, 68, -72, 69, -69, -46, -17, -96, -92, -43, -63, 57, -60, -71,
0, 79, -74, 19, 54, 37, 8, 62, -32, -79, -93, -56, 24, 72, 15, 1, 7, 45, -33, -72, 0, 80, 61, 82, 83, -83, -66, 20, -70, -70, 84, 36, 
-45, -38, -37, 24, 82, 84, -26, -34, -71, -18, -83, 23, -28, 6, -14, -98, 21, -14, 11, 60, 58, 67, -50, 16, -4, 55, 10, 86, 68, 33, -78]: 
медиана - 0
0.009172699999999999
0.5300494
62.4220723

"""

from random import randint
from timeit import timeit

# Гномья сортировка

def gnome(lst):
	i, size = 1, len(lst)
	while i < size:
		if lst[i - 1] <= lst[i]:
			i += 1
		else:
			lst[i - 1], lst[i] = lst[i], lst[i - 1]
			if i > 1:
				i -= 1
	return lst

def my_median(data):

	n = len(data)
	i = n // 2

	if n % 2:
		return f"Для списка - {orig_list}: \n" \
			   f"медиана - {gnome(data)[i]}"
	return f"Для списка - {orig_list}: \n" \
			   f"медиана {sum(gnome(data)[i - 1:i + 1]) / 2}"




m = randint(3, 100)

orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(my_median(orig_list[:]))

# замеры 10
orig_list = [randint(-100, 100) for _ in range(10)]

print(
    timeit(
        "my_median(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "my_median(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "my_median(orig_list[:])",
        globals=globals(),
        number=1000))

