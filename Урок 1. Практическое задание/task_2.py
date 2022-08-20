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
''' Сложность данного алгоритма : O(n)'''
def minimum_value(data):
    low = data[0]
    for i in data:
        if i < low:
            low = i
    return low
print(minimum_value([3,4,5,6,7,8,98,3,4,5,6,7,8,9]))

''' Сложность данного алгоритма : O(n^2)''' # сам не смог сделать, разбирал по готовому коду, вроде дошло
def list_min_f(lst):
    for i in lst:
        is_min = True
        for j in lst:
            if i > j:
                is_min = False
        if is_min:
            return i

print(list_min_f([5,6,7,8,9,5,3,]))



