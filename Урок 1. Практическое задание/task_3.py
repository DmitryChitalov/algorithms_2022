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
import time


def high_profit_1(storage):
    """Общая сложность O(N logN)"""

    sort_storage = sorted(storage.items(), key=lambda x: x[1], reverse=True)    # O(N logN)
    print(f'Три компании с наибольшей годовой прибылью:\n'                      # O(1)
          f'{sort_storage[0][0]} - {sort_storage[0][1]}\n'                      # O(1)
          f'{sort_storage[1][0]} - {sort_storage[1][1]}\n'                      # O(1)
          f'{sort_storage[2][0]} - {sort_storage[2][1]}')                       # O(1)


def high_profit_2(storage):
    """Общая сложность O(N)"""
    res_lst = []                                                  # O(1)
    flag_min = False                                              # O(1)
    for el in storage.items():                                    # O(N)
        if len(res_lst) < 3:                                      # O(1)
            res_lst.append(el)                                    # O(1)
        else:                                                     # O(1)
            if flag_min is False:                                 # O(1)
                min_el = min(res_lst, key=lambda x: x[1])         # известен размер => O(1), выполнить один раз
                flag_min = True                                   # O(1)
            if el[1] <= min_el[1]:                                # O(1)
                continue                                          # O(1)
            else:                                                 # O(1)
                res_lst.append(el)                                # O(1)
                res_lst.sort(key=lambda x: x[1], reverse=True)    # O(N logN), но известен размер => O(1)
                res_lst.pop()                                     # O(1)
                min_el = res_lst[-1]                              # O(1)
    print(f'Три компании с наибольшей годовой прибылью:\n'        # O(1)
          f'{res_lst[0][0]} - {res_lst[0][1]}\n'                  # O(1)
          f'{res_lst[1][0]} - {res_lst[1][1]}\n'                  # O(1)
          f'{res_lst[2][0]} - {res_lst[2][1]}')                   # O(1)


info_storage = {f'Компания_{i}': randint(1000, 100000000) for i in range(1, 10000000)}
st = time.time()
high_profit_1(info_storage)
print(time.time() - st)
print()
st = time.time()
high_profit_2(info_storage)
print(time.time() - st)

""" 
Выводы: второй алгоритм больше в реализации, но заметнее быстрее во времени.
В условии не сказано что делать с фирмами с одинаковой годовой прибылью, этим пренебрёг. 
Замеры в программе оставил, для наглядности. 
На моей машине с такими входными данными первый алгоритм ~ 19 сек., второй ~ 4 сек. 
"""
