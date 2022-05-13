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
from random import randint

def min_1(lst):
    len_lst =  len(lst) #O(1)
    for i in range(len_lst-1): # O(N)
        for j in range(len_lst-i-1): # O(N)
            if lst[j] > lst[j + 1]: # O(1)
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # O(1)

    min_value = lst[0] #O(1)

    return min_value #O(1)

def min_2(lst):
    len_lst = len(lst) #O(1)
    if len_lst == 0: #O(1)
        return None #O(1)

    min_value = lst[0] #O(1)
    for i in range(len_lst): #O(N)
        if lst[i] < min_value: #O(1)
            min_value = lst[i] #O(1)

    return min_value #O(1)

if __name__ == '__main__':

    lst =  [randint(1,99) for _ in range(1,15)]
    print(lst)
    print(f'min_1 = {min_1(lst)}')
    print(f'min_2 = {min_2(lst)}')