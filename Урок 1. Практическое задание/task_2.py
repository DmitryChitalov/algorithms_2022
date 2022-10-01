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

numbers = [10, 8, 12, 6, 14, 4, 16]

# O(n^2)
def min_value_n2(lst): 
    min_number = 0
    for i in range(len(lst)-1): 
        for j in range(i, len(lst)-1):
            if lst[j] < lst[i]:
                min_number = lst[j]
    return min_number

# O(n)
def min_value_n(lst):
    min_number = lst[0]
    for i in lst: 
        if i < min_number:
            min_number = i
    return min_number

print(min_value_n2(numbers))
print(min_value_n(numbers))