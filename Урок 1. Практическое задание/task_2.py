"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


def min_list_n2(mylist):
    for i in range(0, len(mylist) - 1):
        _min = i
        for j in range(i + 1, len(mylist)):
            if mylist[j] < mylist[_min]:
                _min = j
        mylist[i], mylist[_min] = mylist[_min], mylist[i]
    return mylist[0]


def min_list_n(mylist):
    result = mylist[0]
    for i in mylist:
        if result > i:
            result = i
    return result


list1 = [8, 4, -5, 2, 6, 7, 5, 0, -12, -1, 4, 7, 8, -2, -4, -1]
print(min_list_n(list1))
print(min_list_n2(list1))
