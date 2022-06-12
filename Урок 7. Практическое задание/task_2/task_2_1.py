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
from timeit import timeit


def gnome(m):
    data = [randint(0, 10000) for _ in range(2 * m + 1)]
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data[m]


# замер 11
print(timeit("gnome(5)", globals=globals(), number=1000))

# замер 101
print(timeit("gnome(50)", globals=globals(), number=1000))

# замер 1001
print(timeit("gnome(500)", globals=globals(), number=1000))

"""
0.022099420000813552
1.0141220969999267
66.35984792199997
"""