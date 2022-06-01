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


def min_finder_1(lst_obj):                      # O(N^2)
    for i in range(len(lst_obj)):               # O(N)
        for j in range(i + 1, len(lst_obj)):    # O(N)
            if lst_obj[i] < lst_obj[j]:         # O(1)
                return lst_obj[i]               # O(1)


def min_finder_2(lst_obj):                      # O(N)
    min_val = lst_obj[0]                        # O(1)
    for i in range(len(lst_obj)):               # O(N)
        if min_val > lst_obj[i]:                # O(1)
            min_val = lst_obj[i]                # O(1)

    return min_val                              # O(1)


print(min_finder_1([1, 2, 3]))
print(min_finder_2([5, 2, 3]))
