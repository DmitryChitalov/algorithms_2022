"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


def user_bad_min(lst):
    if type(lst) is list:
        sort_list = [lst[0]]
        for i in range(1, len(lst)):
            for ind, num in enumerate(sort_list):
                if num > lst[i]:
                    sort_list.insert(ind, lst[i])
                    break
                elif ind == len(sort_list) - 1:
                    sort_list.append(lst[i])
                    break
    return sort_list[0]


def user_good_min(lst: list):
    if type(lst) is list:
        minimum = lst[0]
        for i in lst[1:]:
            if minimum > i:
                minimum = i
    return minimum


user_lst = [9,5,5,4,7,7,8,9,3,5,8,5,767,5,43,43,90]
print(user_good_min(user_lst))
print(user_bad_min(user_lst))
