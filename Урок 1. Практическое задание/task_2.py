"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
# Сложность  алгоритма O(n) - линейная.
def min_value(sps):
    min = sps[0]
    for i in range(1, len(sps)):
        if sps[i] < min:
            min = sps[i]
    return min

second_lst = [-10, 20, 1, 14, 510, 10, 7, 30, 9, 10, 11, 12, 13, 14, 0]
print(min_value(second_lst))

# Сложность  алгоритма O(n**2)  решение не оптимальное
def min_value_two(sps):
    min = 0
    for n in sps:
        for i in range(len(sps)):
            if n > sps[i]:
                min = sps[i]
    return min

print(min_value_two(second_lst))

