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
from timeit import timeit
from random import randrange


# Гномья сортировка
def find_median(m):
    lst = [randrange(-100, 100) for _ in range(2 * m + 1)]

    def gnome_opt(lst, m):
        i, j, size = 1, 2, len(lst)
        while i < size:
            if lst[i - 1] <= lst[i]:
                i, j = j, j + 1
            else:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                i -= 1
                if i == 0:
                    i, j = j, j + 1
        return lst, lst[m]
    return gnome_opt(lst, m)


print(find_median(2))

print(timeit('find_median(10)', globals=globals(), number=1000))  # 0.0275792
print(timeit('find_median(100)', globals=globals(), number=1000))  # 1.4857689
print(timeit('find_median(1000)', globals=globals(), number=1000))  # 159.09634640000002
