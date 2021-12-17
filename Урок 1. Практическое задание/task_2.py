"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# O(n^2)
list_ = [[9, 2], [3, 7]]
n = list_[0][0]
for i in list_:
    for j in i:
        if j < n:
            n = j
print(n)


# O(n)
list_1 = [8, 2, 3, 4, 5, 7, 8]
n = list_1[0]
for i in range(1, len(list_1)):
    if list_1[i] < n:
        n = list_1[i]
print(n)