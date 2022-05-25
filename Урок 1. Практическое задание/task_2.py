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

def first_min(user_list): # O(n^2)
    start = True # O(1)
    while start: # O(n)
        start = False # O(1)
        for i in range(len(user_list) - 1): # O(n)
            if user_list[i] > user_list[i + 1]: # O(1)
                user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i] # O(1)
                start = True # O(1)
    return user_list[0] # O(1)

def second_min(user_list): # O(n)
    min_el = user_list[0] # O(1)
    for el in user_list: # O(n)
        if min_el > el: # O(1)
            min_el = el # O(1)
    return min_el # O(1)

my_list = [7, 3, 9, 10, 1, 45, 3, 6, 3]
print(first_min(my_list))
print(second_min(my_list))

