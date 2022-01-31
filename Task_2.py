"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
# сложность O(n**2) - квадратичная
def second_min(lst):
    result = lst[0]
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            if j < result:
                result = lst[j]
    return result

# сложность O(n) - линейная
def first_min(lst):
    result = lst[0]
    for i in lst:
        if i < result:
            result = i
    return result

my_lst = [1, 3, 5, 4, 6, 9, 10, 2]

print(first_min(my_lst))
print(second_min(my_lst))