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


from random import randint

ls = [randint(0, 100) for i in range(10)]


# квадратичная сложность
def min_list_1(ls):
    for i in ls:              # O(n)
        val = True            # +
        for n in ls:          # O(n) = O(n^2)
            if i > n:         # O(1)
                val = False   # O(1)
        if val:               # O(1)
            return i          # O(1)


print(ls)
print(min_list_1(ls))


# линейная сложность
def min_list_2(ls):
    val = ls[0]       # O(1)
    for i in ls:      # O(n)
        if i < val:   # O(1)
            val = i   # O(1)
    return val        # O(1)


print(min_list_2(ls))
