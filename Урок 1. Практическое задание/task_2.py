#! +
"""
2021-12-18
Geekbrains. Факультет python-разработки
Студент: Папко Роман.
Четверть 1. Алгоритмы и структуры данных на Python. Базовый курс
Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
Домашнее задание 2.
"""
"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

from random import randint


list_lenght = 30
start_random = -100
end_random = 100

def min_element_sq(lst):  				#!!! O(n**2)
    min_el = lst[0]
    for i in lst:
        for j in lst:
            if i < j:
                smaller = i
            else:
                smaller = j
            if smaller < min_el:
                min_el = smaller
    return min_el

def min_element_lin(lst):  			#!!! O(n)
    min_el = lst[0]
    for i in lst:
        if i < min_el:
            min_el = i
    return min_el


my_list = [randint(start_random, end_random) for _ in range(1, list_lenght + 1)]

print(my_list)
print(min_element_sq(my_list))
print(min_element_lin(my_list))
