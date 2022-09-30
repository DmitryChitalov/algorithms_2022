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

first_list = [100, 50, 3, 4, 23, 10]


# Сложность: O(n^2) два уровня вложенности

def min_number(user_list):
    min_el = user_list[0]
    for i in user_list:  # O(n)
        for j in range(len(user_list)):  # O(n)
            if min_el > user_list[j]:  # O(1)
                min_el = user_list[j]  # O(1)
    return min_el  # O(1)


# Сложность: O(n) линейное время - чем больше элементов, тем дольше выполняется поиск

def min_number_2(user_list):
    min_number = user_list[0]  # O(1)
    for i in range(len(user_list)):  # O(n)
        if user_list[i] < min_number:  # O(1)
            min_number = user_list[i]  # O(1)
    return min_number  # O(1)


print(min_number(first_list))

print(min_number_2(first_list))
