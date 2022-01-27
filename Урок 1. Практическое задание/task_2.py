"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

initial_list = [2222, 3, 6, 3, 76, 4, 555, 33]

# O(n)
min1 = initial_list[0]
for val in initial_list:
    if val < min1:
        min1 = val

print(min1)

# O(n^2)
min2 = initial_list[0]

for val in initial_list:
    for i in initial_list:
        if val < i and min2 > val:
            min2 = val

print(min2)
