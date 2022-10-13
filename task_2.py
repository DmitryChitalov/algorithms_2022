# Задание 2.
# Сложность первого алгоритма должна быть O(n^2) - квадратичная.

lst = [9, 5, 7, 4, 10];

def min_1(list_1):
    res = list_1[0]
    for i in list_1:
        for j in range(list_1.index(i), len(list_1), 1):
            if res > list_1[j]:
                res = list_1[j]
    return res
print(min_1(lst));

# Сложность второго алгоритма должна быть O(n) - линейная.

def min_2(list_2):
    res = list_2[0]
    for i in list_2:
        if i < res:
            res = i
    return res
print(min_2(lst));