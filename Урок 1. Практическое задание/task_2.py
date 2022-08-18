# """
# Задание 2.
#
# Реализуйте два алгоритма.
#
# Оба должны обеспечивать поиск минимального значения для списка.
#
# Сложность первого алгоритма должна быть O(n^2) - квадратичная.
#
# Сложность второго алгоритма должна быть O(n) - линейная.
#
#
# Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
# -- нельзя использовать встроенные функции min() и sort()
# -- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
# -- проставьте сложности каждого выражения в двух ваших алгоритмах
# """
def min_lst(x):
    min_a = x[0]
    idx = 1
    while idx <= (len(x) - 1):
        if min_a > x[idx]:
            min_a = x[idx]
        idx += 1
    return min_a

def min_lst_2(x):
    min_b = x[0]
    for i in x[1:]:
        if i < min_b:
            min_b = i
    return min_b

lst_a = [-3, 1, -5, 1000, -55]
print(f'Минимальное значение в списке: {min_lst(lst_a)}')
print(f'Минимальное значение в списке: {min_lst_2(lst_a)}')

