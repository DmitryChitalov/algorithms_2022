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

# Сложность: O(len(num))
def min_num(num):
    result = 0
    for i in range(len(num)):  # O(N)
        if result > num[i]:    # O(1)
            result = num[i]    # O(1)
    return result


num = [randint(-100, 100) for i in range(30)]
print(min_num(num))

# Сложность: O(n^2)
def find_min(num):
    result = 0
    for i in range(len(num)):    #O(n)
        for j in num:            #(n)
            if j < result:       #O(1)
                result = j       #O(1)
    return result

print(find_min(num))








