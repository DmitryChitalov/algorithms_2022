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


def mediana_2(m):
    lst = [randint(0, m + 10) for i in range(2 * m + 1)]
    count = 0
    lst_1 = lst[:]
    while count < m:
        lst_1.remove(max(lst_1))
        count += 1
    return f'Список: \n{lst}\nМедиана списка: {max(lst_1)}'


print(mediana_2(4))
print(timeit('mediana_2(5)', globals=globals(), number=1000))
print(timeit('mediana_2(50)', globals=globals(), number=1000))
print(timeit('mediana_2(500)', globals=globals(), number=1000))
"""
Результаты замеров:
0.04913020000094548
0.5154567999998108
15.266785299998446
"""