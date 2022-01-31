"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""


def natural_number_series_sum(count):  # Решение через рекурсию.
    if count <= 0:
        return count
    return count + natural_number_series_sum(count - 1)


def cmp_arithmetic_progression_sum(num):
    s0 = num * (num + 1) / 2  # сумма всех членов арифметической последовательности при d=1; a1=0
    s1 = natural_number_series_sum(num)
    if s0 == s1:
        print(f'Верно! Сумма (1...{num}) = {s1} = {num}({num}+1)/2')
    else:
        print(f'Ошибка! Сумма (1...{num}) = {s1} != {num}({num}+1)/2 = {s0}')


cmp_arithmetic_progression_sum(10)
cmp_arithmetic_progression_sum(100)
