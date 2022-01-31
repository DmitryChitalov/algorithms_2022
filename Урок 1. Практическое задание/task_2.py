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


# Первый алгоритм O(n^2)
def min_algorithm1(num_list):
    min_value = num_list[0]
    for i in range(len(num_list)):
        min_value = num_list[i]
        for j in range(len(num_list)):
            if num_list[j] < min_value:
                min_value = num_list[j]
    return min_value


# Второй алгоритм O(n)
def min_algorithm2(num_list):
    min_value = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] < min_value:
            min_value = num_list[i]
    return min_value


if __name__ == "__main__":
    for j in (50, 500, 1000, 5000, 10000):
        # Из 100000 чисел возьмем 'j' случайно выбранных
        # Всего 10 тыс. чисел
        lst = random.sample(range(-100000, 100000), j)

    print('Calculating...')
    print('Algorithm 1:', min_algorithm1(lst))
    print('Algorithm 2:', min_algorithm2(lst))
    print('Min (built-in):', min(lst))
