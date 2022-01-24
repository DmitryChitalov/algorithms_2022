"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.
"""


def min_of_list_1(user_list):

    for i in range(len(user_list)):
        for j in range(len(user_list)):
            if user_list[i] < user_list[j]:
                min_el = user_list[i]
            else:
                min_el = user_list[i]

    return min_el



"""
Сложность второго алгоритма должна быть O(n) - линейная.
"""


def min_of_list_2(user_list):

    min_el = user_list[0]  # O(1)
    for i in range(len(user_list)):  # O(n)
        if user_list[i] < min_el:  # O(1)
            min_el = user_list[i]  # O(1)
    return min_el  # O(1)

    # O(1) + O(n) * (O(1) + O(1)) + O(1) = O(n)


"""
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""