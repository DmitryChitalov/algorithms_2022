"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# Первый вариант алгоритма с O(n**2)

def min_number1(lst):
    for i in range(len(lst)):
        min_number = lst[i]
        for j in lst:
            if min_number > j:
                min_number = j
        break
    return min_number


# Второй вариант алгоритма с O(n)
def min_number2(lst):
    min_number = lst[0]
    for i in lst:
        if i < min_number:
            min_number = i
    return min_number


mylist = [1000, -9, 11, 22, 44444, 7, 883, 10, -5, 0]

print(min_number1(mylist))

print(min_number2(mylist))
