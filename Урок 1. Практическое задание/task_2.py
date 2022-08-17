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


def min_val_in_list(list):      # Квадратичная
    for i in range(0, len(list) - 1):
        min_idx = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list[0]


def min_val_in_list2(list):      # Линейная
    min_val = list[0]
    for i in list:
        if i < min_val:
            min_val = i
    return min_val


mylist = [66, 33, 1, 5, 2, 10]
print(min_val_in_list(mylist))
print(min_val_in_list2(mylist))
