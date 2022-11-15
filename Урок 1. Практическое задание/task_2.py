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
numbers = [7, 4, 22, 17, 19, 44, 3, 51, 14, 17, 35, 99, 28]


def squared_algorithm(number_list):
    useless_list = []  # O(n)
    lowest = number_list[0]  # O(1)      
    for number in number_list:  # O(n)
        useless_list.append(number)  #O(1)
        for numb in useless_list:  # O(n)
            if numb < lowest:  # O(1)
                lowest = numb  # O(1)
            else:  # O(1)
                continue  # O(1)
    print(lowest)
    

def linear_algorithm(number_list):
    lowest = number_list[0]  # O(1)
    for number in number_list:  # O(n)
        if number < lowest:  # O(1)
            lowest = number  # O(1)
        else:  # O(1)
            continue  # O(1)
    print(lowest)


squared_algorithm(numbers)
linear_algorithm(numbers)
