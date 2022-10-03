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


from statistics import median
from timeit import timeit
from random import randint


m = 10
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]


print(f'Медиана: {median(orig_list[:])}')
# замеры 10
print(
    timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))
m = 100
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'Медиана: {median(orig_list[:])}')
# замеры 100
print(
    timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))

m = 1000
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'Медиана: {median(orig_list[:])}')
# замеры 1000
print(
    timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))
"""

ИТОГ:
Результаты тестов первого способа.
(m = 10)
0.0051321000210009515
(m = 100)
0.08724749996326864
(m = 1000)
1.611517199955415

Результаты тестов второго способа.
(m = 10)
0.0016279999981634319
(m = 100)
0.05661400000099093
(m = 1000)
4.510680099949241

Результаты тестов третьего способа.
(m = 10)
0.0005950999911874533
(m = 100)
0.005869399989023805
(m = 1000)
0.1479170999955386

Третий способ самый эффективный. На втором месте способ через сортировку Шелла, на третьем - без сортировки.
Но если сравнивать первый и второй способ, то при работе с небольшими списками выигрывает второй вариант, наверное,
это погрешности.
"""