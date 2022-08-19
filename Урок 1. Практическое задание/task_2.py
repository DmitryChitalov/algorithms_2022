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

lst = [1, 4, 2, 6, 9, 3, 2, 5, 11, -1, 14, 1, 12, 13]


"""
O(n)
"""

print(lst)
def find_min(randList: list):
    min = randList[0]
    for i in randList:
        if i < min:
            min = i
    return min


print(find_min(lst))




"""
O(n^2)
"""
print(lst)


def sort_find_min(randList: list):
    for i in range(len(lst)-1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp


sort_find_min(lst)
print(lst[0])







