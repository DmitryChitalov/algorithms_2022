from random import randint


# Сложность первого алгоритма должна быть O(n^2) - квадратичная
def list_min_f(lst):
    for i in lst:
        is_min = True
        for j in lst:
            if i > j:
                is_min = False
        if is_min:
            return i


# Сложность второго алгоритма должна быть O(n) - линейная
def list_min_s(lst):
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value


lst1 = [randint(0, 100) for i in range(20)]
print(lst1)
print(list_min_f(lst1))
print(list_min_s(lst1))
