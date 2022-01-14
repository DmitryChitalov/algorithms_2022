"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

import random


my_list = random.choices(range(0, 10**6), k=10**2) 

# good_min ==> O(n)
def good_min(sequence):         
    min_number = sequence[0] # O(1)
    for current_number in sequence:  # O(n)
        if min_number > current_number: # O(1)
            min_number = current_number # O(1)
    return min_number # O(1)

# bad_min_1 ==> O(n^2)
def bad_min_1(sequence):  # O(1)                   
    for i1 in range(len(sequence)):   # O(n)
        for i2 in range(i1 + 1, len(sequence)):  # O(n)
            if sequence[i1] > sequence[i2]:  # O(1)
                sequence[i1], sequence[i2] = sequence[i2], sequence[i1]  # O(1)
    return sequence[0] 

# bad_min_2 ==> O(n^2)
def bad_min_2(sequence):  # O(1)
    inner_sequence = list(sequence) # O(n)
    min_number = inner_sequence.pop(0) # O(n)
    while inner_sequence: # O(n)
        current_number = inner_sequence.pop(0) # O(n)
        if min_number > current_number: # O(1)
            min_number = current_number # O(1)
    return min_number # O(1)

print(good_min(my_list))
print(bad_min_1(my_list))
print(bad_min_2(my_list))
