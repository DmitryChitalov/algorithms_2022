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




def find_min_value_1(lst: list):
    '''
    Функция находит минимальное значение в списке

    Сложность: O(n^2)     T(n) = n(1+n(1+1)+1+1) = 2n^2 + 3n

    :param lst: list
    :return: float
    '''

    for i in range(len(lst)):               # O(n)
        count = 0                           # O(1)
        for j in range(len(lst)):           # O(n)
            if lst[i] > lst[j]:             # O(1)
                count += 1                  # O(1)
        if count == 0:                      # O(1)
            return lst[i]                   # O(1)


def find_min_value_2(lst: list):
    '''
    Функция находит минимальное значение в списке

    Сложность: O(n)      T(n) = 1 + n(1+1) 1 = 2n + 2

    :param lst: list
    :return: float
    '''
    min_num = float('inf')                   # O(1)
    for num in lst:                          # O(n)
        if num < min_num:                    # O(1)
            min_num = num                    # O(1)
    return min_num                           # O(1)






num_list = [2, 8, 10, 5, 2, 3, -5.2, 1, 9]

print(find_min_value_1(num_list))
print(find_min_value_2(num_list))
