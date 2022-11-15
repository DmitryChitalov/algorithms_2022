"""
Сложность: O(1)
Название: постоянное время (сложность - константа)

Время работы алгоритма не зависит от объема входящих данных
"""


first_lst = ["one", "two", "three", "four"]
second_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def get_lst_func(lst):
    length = len(lst)  # O(1)
    return length  # O(1)


print(get_lst_func(first_lst))
print(get_lst_func(second_lst))
