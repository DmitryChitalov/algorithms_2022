"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def sum_of_natural_numbers(natural_number, current_sum_of_natural_numbers):
    if natural_number == 0:
        return current_sum_of_natural_numbers
    else:
        current_sum_of_natural_numbers += natural_number
        return sum_of_natural_numbers(natural_number - 1, current_sum_of_natural_numbers)


maximum_natural_number = int(input("Введите максимальное натуральное число:"))


if sum_of_natural_numbers(maximum_natural_number, 0) == maximum_natural_number * (maximum_natural_number + 1)/2:
    print("Равенство 1+2+...+n = n(n+1)/2 верно!")

