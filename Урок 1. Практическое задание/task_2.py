"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
# Имена переменных приведены к нормам PEP8
lst_vals = [ 0, -1, 10, -25, 100, -3]

# O(n**2)
def search_min_quadratic(lst_vals):
    for i in lst_vals:                               # O(n)
        if i < lst_vals[0]:                          # O(1)
            lst_vals.insert(0, lst_vals[lst_vals.index(i)])  # O(n)
    return lst_vals[0]


# O(n)
def search_min_linear(lst_vals):
    val_min = lst_vals[0]       #O(1)
    for i in lst_vals:      #O(n)
        if i < val_min:     #O(1)
            val_min = i     #O(1)
    return val_min

print("Минимальный элемент: ", search_min_quadratic(lst_vals))
print("Минимальный элемент: ", search_min_linear(lst_vals))