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


def first_alg(lst: list) -> int:  # O(n^2)

    for itm in lst:  # O(n)
        itm_is_min = True  # O(1)
        for itm2 in lst:  # O(n)
            if itm2 < itm:  # O(1)
                itm_is_min = False  # O(1)
        if itm_is_min:  # O(1)
            return itm  # O(1)


def second_alg(lst: list) -> int:  # O(n)

    result = lst[0]  # O(1)
    for itm in lst:  # O(n)
        if itm < result:  # O(1)
            result = itm  # O(1)

    return result  # O(1)


if __name__ == '__main__':
    my_list = [1, 4, 3, 2, 45, 6, -2, 15]

    print(my_list)
    print(first_alg(my_list))
    print(second_alg(my_list))
