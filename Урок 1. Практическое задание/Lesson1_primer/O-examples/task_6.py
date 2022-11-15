"""
Сложность: O(n)
Название: линейная сложность

Время возрастает линейно и прямо пропорционально количеству передаваемых данных
"""


first_lst = ["one", "two", "three", "four"]
second_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def get_lst_func(lst):
    for el in lst:
        print(el)


get_lst_func(first_lst)
print()
get_lst_func(second_lst)
