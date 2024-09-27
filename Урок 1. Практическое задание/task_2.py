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
import random

n_num = 10
user_list = [2, 3, 9, 34, 1, 90, 67, 25, 8]
num = [num for num in range(0, 100)]
num_list = list(random.sample(num, n_num))
print(num_list)

# Реализуем квадротичный поиск O(n^2).
def min_of_list_1(user_list):
    for i in range(len(user_list)):
        min_el = user_list[i]
        for j in range(len(user_list)):
            if min_el < user_list[j]:
                pass
            else:
                min_el = user_list[j]

    return min_el


print(min_of_list_1(user_list))
print(min_of_list_1(num_list))

# Реализуем линейный поиск O(n).

def min_of_list_2(user_list):

    min_el = user_list[0]  # O(1)
    for i in range(len(user_list)):  # O(n)
        if user_list[i] < min_el:  # O(1)
            min_el = user_list[i]  # O(1)
    return min_el  # O(1)

print(min_of_list_2(num_list))
print(min_of_list_2(user_list))
# O(1) + O(n) * (O(1) + O(1)) + O(1) = O(n)

# Результат выполнения функций одинаков