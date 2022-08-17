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

def search_of_min_1(list):
    #O(n) - линейная
    min_number = list[0]          # O(1)
    for number in list:           # O(N)
        if number < min_number:   # O(1)
            min_number = number   # O(1)
    return min_number             # O(1)


def search_of_min_2(list):
    # O(nˆ2) - квадратичная
        length = len(list) # O(1)
        for i in range(length - 1): # O(N)
            for j in range(0, length - i - 1): # O(N)
                if list[j] > list[j + 1]:  # O(1)
                    list[j], list[j + 1] = list[j + 1], list[j]  # O(1)

import random
rndm_list=[]
for i in range(0,10):
    number = random.randint(1,30)
    rndm_list.append(number)
print(rndm_list)

print(search_of_min_1(rndm_list)) #1

search_of_min_2(rndm_list) #2
print(rndm_list[0])
