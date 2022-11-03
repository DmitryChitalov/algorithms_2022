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

# O(N**2)

def min_num(num_list):

    min_number = num_list[0] # O(1)
    for i in num_list: # O(N)
        for j in range(len(num_list)): # O(N)
            if min_number > num_list[j]: # O(1)
                min_number = num_list[j] # O(1)
    return min_number # O(1)


print(min_num([55, 21, 44, 8, 11, 33, 344, 9, 3, 22, 4]))

# O(N)

def min_num2(num_list):

    min_number = num_list[0] # O(1)

    for j in range(len(num_list)): # O(N)
        if min_number > num_list[j]: # O(1)
            min_number = num_list[j] # O(1)
    return min_number # O(1)

print(min_num2([55, 21, 44, 8, 11, 33, 344, 9, 1, 22, 4]))