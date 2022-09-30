"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.
соответствует

Сложность второго алгоритма должна быть O(n) - линейная.
соответствует

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

def min_value1(lst1):                   # O(N^2)
    result = lst1[0]                    # O(1)
    for i in range(1, len(lst1)):       # O(N)
        for j in range(i, len(lst1)):   # O(N)
            if lst1[j] < result:        # O(1)
                result = lst1[j]        # O(1)
    return result                       # O(1)


def min_value2(lst1):                   # O(N)
    result = lst1[0]                    # O(1)
    for el in lst1[1:]:                 # O(N)
        if el < result:                 # O(1)
            result = el                 # O(1)
    return result  # O(1)               # O(1)





if __name__ == '__main__':
    li = (16, 17, 15, 18, 14, 19, 13)

    print(' procedure min_value1')
    print(min_value1(li))
    print(' procedure min_value2')
    print(min_value2(li))
