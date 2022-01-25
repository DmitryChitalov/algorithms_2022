"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

# Алгоритм 1


first_list = [45, 54645, 25324, -875678, 2342423, 1231, 4, -5, -1000000, 45646, -3453, 3453, 2344, 123, -345345, 456]


for index in range(len(first_list) - 1):
    if first_list[index] < first_list[index + 1]:
        first_list[index + 1] = first_list[index]


print(first_list[len(first_list) - 1])


# Алгоритм 2


second_list = [45, 546454, 25324, -7875678, 2342423, 1231, 4, -5, -10000,
               45646, -63453, 3453, 2344, 12456453, -345345, 456,475734636]


min_member_of_list = second_list[0]
for member in second_list[1:]:
    if member < min_member_of_list:
        min_member_of_list = member


print(min_member_of_list)








