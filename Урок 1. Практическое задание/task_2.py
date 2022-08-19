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


# Первый вариант. Линейная сложность O(n).
def linear_decision(new_list):
    min_number = new_list[0]
    for i in new_list:
        if i < min_number:
            min_number = i
    return min_number


# Второй вариант. Квадратичная сложность O(n^2).
def quadratic_decision(new_list):
    min_number_2 = new_list[0]
    for i in new_list:
        for a in range(new_list.index(i) + 1, len(new_list) - 1, 1):
            if min_number_2 > new_list[a]:
                min_number_2 = new_list[a]
    return min_number_2


task_2_list = [15, 64, 70, 5, 82, 107, 19]

print(linear_decision(task_2_list))

print(quadratic_decision(task_2_list))
