"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

from random import sample

list_rnd_num = sample(range(-100, 500), 15)
print(list_rnd_num)

# 1: O(n)
min_num = list_rnd_num[0]
for el in list_rnd_num:
    if el < min_num:
        min_num = el

print(min_num)

# 2: O(n^2)
min_num = list_rnd_num[0]
for i in list_rnd_num:
    for j in range(list_rnd_num.index(i) + 1, len(list_rnd_num) - 1, 1):
        if list_rnd_num[j] < min_num:
            min_num = list_rnd_num[j]

print(min_num)
