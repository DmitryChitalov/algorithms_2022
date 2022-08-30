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
from random import sample
from time import time


def timer(func):
    def wrapper(*args):
        start_time = time()
        return_value = func(*args)
        print(f'Время выполнения - {time() - start_time:.5f}')
        return return_value

    return wrapper


@timer
def min_square(my_list):  # Сложность O(n^2)
    for i in range(len(my_list)):
        flag = True  # Предположим, что член списка с номером и - минимальный
        for j in range(len(my_list)):
            if i != j and my_list[i] > my_list[j]:  # Проверяем, сравнивая. Если он не миниммльный, то...
                flag = False
                break
        if flag:
            return my_list[i]


@timer
def min_linear(my_list):
    minimum = my_list[0]
    for i in my_list:
        if i < minimum:
            minimum = i
    return minimum


lst = sample(range(-100000, 100000), 20000)
print(min_linear(lst))
print(min_square(lst))
print(min(lst))
