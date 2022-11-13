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


def winners_1(dic: dict, n: int):
    '''
    Словарь и возвращает словарь из n ключ-значений с максимальным значением

    Сложность: O(n^2)     T(n) = n+n*logn + 1 + n(1 + n(1+1))+1 = 2n^2 + n*logn + 2n +2

    :param dic:dict
    :param n:int
    :return:dict
    '''
    sorted_values = sorted(dic.values())        # O(n)+O(n logn)
    result = {}                                 # O(1)
    for _ in range(n):                          # O(n)
        val = sorted_values.pop()               # O(1)
        for key, item in comp_dict.items():     # O(n)
            if item == val:                     # O(1)
                result[key] = item              # O(1)
    return result                               # O(1)


def winners_2(dic: dict, n: int):
    '''
    Словарь и возвращает словарь из N ключ-значений с максимальным значением

    Сложность: O(n^2)     T(n) = n + n*logn + 1 + n + n(n+1) + 1 = n^2 + n*logn + 3n + 2

    :param dic:dict
    :param n:int
    :return:dict
    '''
    sorted_values = sorted(dic.values())       # O(n)+O(n logn)
    result = {}                                # O(1)
    sorted_values = sorted_values[-n:]         # O(n)
    for key, item in comp_dict.items():        # O(n)
        if item in sorted_values:              # O(n)
            result[key] = item                 # O(1)
    return result                              # O(1)


def winners_3(dic: dict, n: int):
    '''
    Словарь и возвращает словарь из N ключ-значений с максимальным значением

    Сложность: n*logn     T(n) = n + n + n*logn + 1 + n(1 + 1 + 1)+1 = n*logn + 5n + 2

    :param dic:dict
    :param n:int
    :return:dict
    '''
    sorted_dic = sorted(dic.items(), key=lambda item: item[1])  # O(n)+O(n)+O(n logn)
    result = {}                                                 # O(1)
    while n != 0:                                               # O(n)
        el = sorted_dic.pop()                                   # O(1)
        result[el[0]] = el[1]                                   # O(1)
        n -= 1                                                  # O(1)
    return result                                               # O(1)


comp_dict = {'Google': 25000, 'VW': 10000, 'Tesla': 50000, 'BP': 40000, 'Shell': 35000, 'Apple': 48000, 'Nokia': 200}
n = 3
print(winners_1(comp_dict, n))
print(winners_2(comp_dict, n))
print(winners_3(comp_dict, n))

# Алгоритмы функций winners_1 и winners_2 квадратичные по сложности выполнения.
# Но второй будет все же быстрее, т.к. в первом случае n^2 умножается еще на два
# Алгоритм winners_3 линейно-логарифмический по сложности и поэтому выигрывает.
# В алгоритме есть два цикла, но они не вложенные.