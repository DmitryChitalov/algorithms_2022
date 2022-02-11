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

def find_min_1(my_list): # общая сложность O(N)
    min_num = my_list[0] # O(1)
    for i in range(1, len(my_list)): # O(N)
        if my_list[i] < min_num: # O(1)
            min_num = my_list[i] # O(1)
    return min_num # O (1)

sample_list = [44, 50, 0, -2, 999, -49]
print(find_min_1(sample_list))

def find_min_2(my_list): # общая сложность O(N^2)
    for i in my_list: # O(N)
        min_num = True # O(1)
        for j in my_list: # O(N)
            if i > j: # O(1)
                min_num = False # O(1)
        if min_num: # O(1)
            return i # O(1)

sample_list = [44, 50, 0, -2, 999, -49]
print(find_min_2(sample_list))
