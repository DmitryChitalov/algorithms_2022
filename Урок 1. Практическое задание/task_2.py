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
task_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_val = task_list[0] + 1

for val in task_list:
    for i in task_list:
        if val < i and min_val > val:
            min_val = val

print(min_val)


# O(n)
min_val = task_list[0] + 1
for val in task_list:
    if val < min_val:
        min_val = val

print(min_val)
