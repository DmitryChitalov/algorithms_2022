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

def min1(listElements):

    minValue = listElements[0]      # O(1)

    for element in listElements:    # O(N)
        if element < minValue:      # O(len(n))
            minValue = element      # O(1)

    return minValue                 # O(1)


def min2(listElements):

    for element1 in listElements:      # O(N)
        isMin = True                   # O(1)

        for element2 in listElements:  # O(N)
            if element1 > element2:    # O(len(n))
                isMin = False          # O(1)

        if isMin:                      # O(1)
            return element1            # O(1)
