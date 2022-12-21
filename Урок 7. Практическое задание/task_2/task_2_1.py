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


def gnom(data):
    i = 0
    stop =len(data)
    while True:
        if i + 1 == stop:
            return data
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            if i == 0:
                i += 1
            else:
                i -= 1
        else:
            i += 1

m_10 = 10
m_100 = 100
m_1000 = 1000
lst_10 = [randint(1, 100) for _ in range(2 * m_10 + 1)]
lst_100 = [randint(1, 100) for _ in range(2 * m_100 + 1)]
lst_1000 = [randint(1, 100) for _ in range(2 * m_1000 + 1)]
print(f'Исходный массив в 10 эллементов:                {lst_10}')
print(f'Сортированный массив в 10 эллементов:           {gnom(lst_10[:])}')
print(f'Медиана сортированного массива в 10 эллементов: {gnom(lst_10[:])[10]}')
print('-----------------------------------------------------------------')
print('Время массива в 10 эллементов:   ', end='')
print(timeit('gnom(lst_10[:])', globals=globals(), number=100))
print('Время массива в 100 эллементов:  ', end='')
print(timeit('gnom(lst_100[:])', globals=globals(), number=100))
print('Время массива в 1000 эллементов: ', end='')
print(timeit('gnom(lst_1000[:])', globals=globals(), number=100))

'''
Результаты работы метода:
-----------------------------------------------------------------
Время массива в 10 эллементов:   0.00020649999999999835
Время массива в 100 эллементов:  0.36652949999999995
Время массива в 1000 эллементов: 42.7713488
'''
