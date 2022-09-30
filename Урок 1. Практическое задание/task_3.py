"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
from random import randint


def sort_1(dct, k):  # O(N log N)
    from operator import itemgetter
    sorted_dct = dict(sorted(dct.items(), key=itemgetter(1), reverse=True)[:k])  # O(N log N)
    return sorted_dct  # O(1)


def sort_2(dct, k):  # O(N log N)
    from heapq import nlargest
    sorted_keys = nlargest(k, dct, key=dct.get)  # O(N log N)
    sorted_dct = {}  # O(1)
    for j in sorted_keys:  # O(N)
        sorted_dct[j] = dct[j]  # O(1)
    return sorted_dct  # O(1)


def sort_3(dct):  # O(N)
    m1 = ['', 0]  # O(1)
    m2 = ['', 0]  # O(1)
    m3 = ['', 0]  # O(1)

    for key in dct:  # O(N)
        value = dct.get(key)  # O(1)

        if m1[1] < value:  # O(1)
            m3[0], m3[1] = m2[0], m2[1]  # O(1)
            m2[0], m2[1] = m1[0], m1[1]  # O(1)
            m1[0], m1[1] = key, value  # O(1)
        elif m2[1] < value:  # O(1)
            m3[0], m3[1] = m2[0], m2[1]  # O(1)
            m2[0], m2[1] = key, value  # O(1)
        elif m3[1] < value:  # O(1)
            m3[0], m3[1] = key, value  # O(1)
    return (m1, m2, m3)  # O(1)

    """
    Метод 1, 2 сложность одна и таже O(N log N), любая встроенная сортировка требует N log N
    Метод 3 сложность O(N)
    Метод 4 успею переделаю 3 под любое количество максимальных значений k.
    Если k будет придлижаться к N сложность будет O(N**2 log N)
    """


comp = {}
# {'c0': 1634, 'c1': 17881, 'c2': 14199, 'c3': 30879, 'c4': 16532}
for i in range(50):
    comp['c' + str(i)] = randint(0, 50000)

print(comp)
k = 3
print(sort_1(comp, 3))
print(sort_2(comp, 3))
print(sort_3(comp))
