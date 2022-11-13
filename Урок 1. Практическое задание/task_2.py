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
def find_min1(lst):         #O(1)
    if len(lst) > 0:        #O(n)
        minimum = lst[1]    #O(1)
        for i in lst:       #O(n)
            if i < minimum: #O(1)
                minimum = i #O(1)
    else:   
        minimum = None      #O(1)
    return minimum

#Сложность О(n^2)
def find_min2(lst):
    if len(lst) > 0:        #O(n)                   
        minimum = lst[3]    #O(1)
        for i in range(0, len(lst) // 2 + 1):       #O(n)
            for j in range(1, len(lst) // 2 + 1):   #O(n)
                if lst[i] < minimum:                #O(1)
                    minimum = lst[i]                #O(1)
                elif lst[-j] < minimum:             #O(1)
                    minimum = lst[-j]               #O(1)
    else:
        minimum = None      #O(1)
    return minimum


lst1 = [1000, 45, 387,8]
print(find_min1(lst1))

lst2 = [1000, 45, 387,58, 8, 86, 1, 10, 10]
print(find_min2(lst2))