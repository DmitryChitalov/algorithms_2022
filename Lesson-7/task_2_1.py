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


# Гномья сортировка
def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


# замер 10:  0.10679479999816976
m = 10
my_array = [randint(1, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "gnome(my_array[:])",
        globals=globals(),
        number=1000))

print('исходный массив:', my_array)
print('отсортированный массив:', gnome(my_array[:]))
print('медиана: ', gnome(my_array[:])[m])

# замер 100:  7.129075800010469
m = 100
my_array = [randint(1, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "gnome(my_array[:])",
        globals=globals(),
        number=1000))

print('исходный массив:', my_array)
print('отсортированный массив:', gnome(my_array[:]))
print('медиана: ', gnome(my_array[:])[m])

# замер 1000:  896.0709299000009
m = 1000
my_array = [randint(1, 100) for _ in range(2 * m + 1)]
print(
    timeit(
        "gnome(my_array[:])",
        globals=globals(),
        number=1000))

print('исходный массив:', my_array)
print('отсортированный массив:', gnome(my_array[:]))
print('медиана: ', gnome(my_array[:])[m])

# для массива из 1000 элементов очень очень и очень долгая сортировка.
