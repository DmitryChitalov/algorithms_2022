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

# Сложность первого алгоритма O(n^2)


def min_num_buble(num_list):
    last_el = len(num_list)-1      # O(1)
    for el in range(0, last_el):      # O(n)
        for i in range(0, last_el):      # O(n)
            if num_list[i] > num_list[i+1]:     # O(1)
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]     # O(1)
    return num_list[0]      # O(1)


print(min_num_buble([12, 4, 7, 9, 77, 2]))


# Сложность второго алгоритма O(n)


def min_num(num_list):
    min_value = num_list[0]     # O(1)
    for el in num_list:      # O(n)
        if el < min_value:     # O(1)
            min_value = el     # O(1)
    return min_value     # O(1)


print(min_num([12, 4, 7, 9, 77, 2]))
