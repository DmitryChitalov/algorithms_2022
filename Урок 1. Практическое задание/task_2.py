"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго  алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


list = [2,4,7,6,5,5,234,1,6,9,7]
'''O(n)'''


def complex_On(data):
    a = data[0]  # O(1)
    for i in range(len(data)):  # O(n)
        if a > data[i]:  # O(1)
            a = data[i]  # O(1)
    return a  # O(1)


'''O(n^2)'''


def complex_On2(data):
    a = data[0]  ##O(1)
    for number in data:  # O(n)
        for i in range(len(data)):  # O(n)
            if a > data[i]:  # O(1)
                a = number  # O(1)
    return a


print(complex_On(list))
print(complex_On2(list))
