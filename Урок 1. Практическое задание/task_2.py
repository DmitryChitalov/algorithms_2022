"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
from random import randint


# Чтобы реализовать первый алгоритма O(n^2), список д.б. с вложенными списками (матрица)
# либо произвести сортировку одномерного массива и вытащить крайний
# Сортировка выбором
def get_min_quadratic(lst0):
    for i in range(len(lst0) - 1):
        for j in range(i + 1, len(lst0)):
            if lst0[j] < lst0[i]:
                lst0[j], lst0[i] = lst0[i], lst0[j]
    return lst[0]


# Сложность алгоритма O(n) - линейная. Цикл по эл-там списка. n - кол-во эл-тов.
def get_min_linear(lst0):
    min_val = lst0[0]
    for val in lst0:
        if val < min_val:
            min_val = val
    return min_val


lst = [randint(-100, 100) for i in range(randint(0, 50))]  # формируем массив
print(f'{lst=}')
print(f'{get_min_quadratic(lst)=}')
print(f'Sorted {lst=}')
print(f'{get_min_linear(lst)=}')

