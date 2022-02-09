"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

from random import sample

rnd_list = sample(range(-100, 100), 20)
print(rnd_list)

# 1: O(n)
min_num = rnd_list[0]
for el in rnd_list:
    if el < min_num:
        min_num = el

print(f'Минимальное число O(n): {min_num}')

# 2: O(n^2)
min_num = rnd_list[0]
for i in rnd_list:
    for j in range(rnd_list.index(i), len(rnd_list), 1):
        if rnd_list[j] < min_num:
            min_num = rnd_list[j]
print(f'Минимальное число O(n^2): {min_num}')



