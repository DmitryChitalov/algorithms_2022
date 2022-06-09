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

def min_1(list_1):
    len_list =  len(list_1) # O(1)
    for i in range(len_list - 1): # O(N)
        for j in range(len_list - i - 1): # O(N)
            if list_1[j] > list_1[j + 1]: # O(1)
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j] # O(1)

    min_val = list_1[0] # O(1)

    return min_val # O(1)

def min_2(list_1):
    len_list = len(list_1) # O(1)
    if len_list == 0: # O(1)
        return None # O(1)

    min_val = list_1[0] # O(1)
    for i in range(len_list): # O(N)
        if list_1[i] < min_val: # O(1)
            min_val = list_1[i] # O(1)

    return min_val # O(1)

if __name__ == '__main__':

    list_1 =  [randint(1,99) for n in range(1,10)]
    print(list_1)
    print(f'min_1 = {min_1(list_1)}')
    print(f'min_2 = {min_2(list_1)}')
