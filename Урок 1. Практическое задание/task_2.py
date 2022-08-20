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

from random import sample


for j in (50, 500, 1000, 5000, 10000):
    '''Создаю список со случайным набором цифр'''
    lst = sample(range(-100000, 100000), j)


def min_quadratic(list_obj: list):
    '''Возможно перемудрил, но квадратичная сложность'''
    k = 0
    min_el = list_obj[k]
    for element in list_obj:
        k += 1
        if min_el > element:
            min_el = element
            for el in list_obj[k:]:
                if min_el > el:
                    min_el = el
    return min_el


def min_line(list_obj: list):
    '''Линейная сложность нахождения минимального значения'''
    min_el = list_obj[1]                     # константа
    for index in range(len(list_obj) - 1):   # линейная
        if min_el > list_obj[index]:         # константа
            min_el = list_obj[index]         # константа
    return min_el                            # константа


print(f'{min(lst)} - данные для проверки правильности результата')
print(f'{min_line(lst)} - оптимальное решение')
print(f'{min_quadratic(lst)} - непонятное решение =))')