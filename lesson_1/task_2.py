"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
# 1) O(n^2)
def find_min_two(lst2):
    for x in lst2:
        minim = True
        for y in lst2:
            if x > y:
                minim = False
        if minim:
            return(x)

# 2) O(n)
def find_min_one(lst1):
    i = lst1[0]
    for x in range(1, len(lst1)):
        if lst1[x] < i:
            i = lst1[x]
    return i


lst = [2, 5, 1, 4, 25, 7]
print(find_min_two(lst))
print(find_min_one(lst))




