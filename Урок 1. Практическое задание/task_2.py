"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# Сложность линейная O(n)
def minimal_number1(lst):
    min_num = lst[0]
    for i in num_list:
        if i < min_num:
            min_num = i
    return min_num


# Сложность квадратичная O(n**2)
def minimal_number2(lst):
    min_num = 0
    for n in num_list:
        for i in range(len(num_list)):
            if n > num_list[i]:
                min_num = num_list[i]
    return min_num


num_list = [750, 378, 430, 545, 359, 725, 943, 373, 143, 483, 215, 652, 194, 30, 841, 978, 902, 702, 824, 622, 289, 105]
print(minimal_number1(num_list))
print(minimal_number2(num_list))