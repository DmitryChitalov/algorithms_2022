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


def med_no_sort(m):
    lst_obj = [randint(-100, 100) for _ in range(2 * m + 1)]

    for i in range(int((len(lst_obj) - 1) / 2)):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)


# print(med_no_sort(5))

print(timeit("med_no_sort(5)", globals=globals(), number=1000))
print(timeit("med_no_sort(50)", globals=globals(), number=1000))
print(timeit("med_no_sort(500)", globals=globals(), number=1000))

"""
Результаты замеров:
0.023184499994385988
0.2550615999789443
10.277949400013313
"""
