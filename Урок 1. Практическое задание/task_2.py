"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

# Сложность O(n**2)

my_lst = [3, 4, 0, -7, 8]
min_value = my_lst[0]

for i in range(len(my_lst)):            # O(n)
    min_value = my_lst[i]               # O(1)
    for j in range(len(my_lst)):        # O(n)
        if my_lst[j] < min_value:       # O(1)
             min_value = my_lst[j]      # O(1)

# Сложность O(n)

min_value = my_lst[0]                   # O(1)
for i in range(len(my_lst)):            # O(n)
    if my_lst[i] < min_value:           # O(1)
        min_value = my_lst[i]           # O(1)

print(min_value)
