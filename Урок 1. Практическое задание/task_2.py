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

#Сложность О(n)
def find_min1(lst):
    if len(lst) > 0:
        minimum = lst[1]
        for i in lst:
            if i < minimum:
                minimum = i
    else:
        minimum = None
    return minimum

#Сложность О(n^2)
def find_min2(lst):
    if len(lst) > 0:
        minimum = lst[3]
        for i in range(0, len(lst) // 2 + 1):
            for j in range(1, len(lst) // 2 + 1):
                if lst[i] < minimum:
                    minimum = lst[i]
                elif lst[-j] < minimum:
                    minimum = lst[-j]
    else:
        minimum = None
    return minimum


lst1 = [1000, 45, 387,8]
print(find_min1(lst1))

lst2 = [1000, 45, 387,58, 8, 86, 1, 10, 10]
print(find_min2(lst2))