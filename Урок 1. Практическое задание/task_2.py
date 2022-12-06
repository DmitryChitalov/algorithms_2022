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

# Сложность O(n^2)

def min_value_1(user_list):
    lowest_value_1 = user_list[0]                                        # O(1)
    for i in user_list:                                                  # O(n)
        for j in range(user_list.index(i) + 1, len(user_list) - 1, 1):   # O(n)
            if lowest_value_1 > user_list[j]:                            # O(len(user_list[j])
                lowest_value_1 = user_list[j]                            # O(1)

    return lowest_value_1                                                # O(1)


# Сложность O(n)

def min_value_2(user_list):
    lowest_value_2 = user_list[0]     # O(1)
    for i in user_list:               # O(n)
        if i < lowest_value_2:        # O(len(i)
            lowest_value_2 = i        # O(1)

    return lowest_value_2             # O(1)


user_list = [4, 5, 6, 2, 1, 90, 43]

print(min_value_1(user_list))
print(min_value_2(user_list))