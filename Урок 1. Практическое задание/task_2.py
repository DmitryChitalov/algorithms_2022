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


# O(n^2)

def min_of_list1(my_list):
    for i in my_list:  # O(n)
        min_val = True  # O(1)
        for j in my_list:  # O(n)
            if i > j:  # O(1)
                min_val = False  # O(1)
        if min_val:  # O(1)
            return i  # O(1)


# O(n)

def min_of_list2(my_list):
    min_val = my_list[1]  # O(1)
    for i in my_list:  # O(n)
        if i < min_val:  # O(1)
            min_val = i  # O(1)
    return min_val  # O(1)


my_list = [12, 2, 3, 4, 5]
print(my_list)
print(min_of_list1(my_list))
print(min_of_list2(my_list))
