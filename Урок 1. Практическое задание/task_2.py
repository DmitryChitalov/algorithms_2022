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

# O(n) - линейная

lst_1 = [3, 6, 45, -78, 23, 2, -3, -23]


def min_elem(lst_obj):
    min_value = lst_obj[0]      # O(1)
    for elem in lst_obj:        # O(n)
        if elem < min_value:
            min_value = elem     # O(1)
        else:
            continue
    return min_value             # O(1)

print(min_elem(lst_1))

#O(n^2) - квадратичная

def min_elem_2(lst_obj):
    for elem in lst_obj:           # O(n)
        is_min = True              # O(1)
        for min_value in lst_obj:  # O(n)
            if elem > min_value:
                is_min = False     # O(1)
                break
        if is_min:
            return elem            # O(1)

print(min_elem_2(lst_1))
