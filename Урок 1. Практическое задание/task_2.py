"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
# сложность O(n)
def learn_min_meaning(lst):
    min_meaning = lst[0] if lst else None
    for i in range(1, len(lst)):
        if lst[i] < min_meaning:
            min_meaning = lst[i]
    return min_meaning

# Сложность O(n**2)
def learn_min_meaning2(lst):
    min_meaning2 = lst[0] if lst else None
    for i in lst:
        for j in range(1, len(lst)):
            if min_meaning2 > lst[j]:
                min_meaning2 = lst[j]
        return min_meaning2


training_list = [15, 59, 99, 11, 57, 7, 102, 1]

print(learn_min_meaning(training_list))
print(learn_min_meaning2(training_list))