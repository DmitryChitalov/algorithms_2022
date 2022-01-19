"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
lst_in = [0, -1, 10, -25, 100, -3]

# O(n**2)
def search_min_quadratic(lst_in):
    for i in lst_in:                               # O(n)
        if i < lst_in[0]:                          # O(1)
            lst_in.insert(0, lst_in[lst_in.index(i)])  # O(n)
    return lst_in[0]


# O(n)
def search_min_linear(lst_in):
    min_linear = lst_in[0]       #O(1)
    for i in lst_in:            #O(n)
        if i < min_linear:     #O(1)
            min_linear = i     #O(1)
    return min_linear

print("Минимальный элемент: ", search_min_quadratic(lst_in))
print("Минимальный элемент: ", search_min_linear(lst_in))

#исправлено нарушение PEP-8 - заменены имена переменных