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
from random import sample


##############################################################################
"""
Сложность: O(NlogN). O(1) + (O(N) + O(1)) + O(1) + 
                          + O(NlogN) + O(N) + O(1) + O(1) = O(NlogN)
"""


def check_1(dict_obj):
    profit, automakers = [], []              # O(1)
    for i in dict_obj:                       # O(N)
        profit.append(i)                     # O(1)
    profit.sort(reverse=True)                # O(NlogN)
    for j in profit[:3]:                     # O(N)
        automakers.append(dict_obj[j])       # O(1)
    return automakers                        # O(1)


##############################################################################
"""
Сложность: O(N^2). O(1) + (O(N) + O(1)) + (O(N) * O(N) + O(1) + O(1)) +
                        + O(N) + O(1) + O(1) = O(N^2)
"""


def check_2(dict_obj):
    profit, automakers, profit_max = [], [], []       # O(1)
    for i in dict_obj:                                # O(N)
        profit.append(i)                              # O(1)
    for k in range(3):                                # O(N)
        x = max(profit)                               # O(N)
        x = profit.index(x)                           # O(1)
        profit_max.append(profit.pop(x))              # O(1)
    for j in profit_max:                              # O(N)
        automakers.append(dict_obj[j])                # O(1)
    return automakers                                 # O(1)


automakers_orig = ('Mercedes', 'Opel', 'Suzuki', 'Toyota',
                   'UAZ', 'Vaz', 'Subaru')
profit_orig = sample(range(100000, 100000000), len(automakers_orig))
auto_pro = dict(zip(profit_orig, automakers_orig))

print(f'Первое решение: {check_1(auto_pro)}')
print(f'Второе решение: {check_2(auto_pro)}')

"""
Выводы:
Первое решение более эффективно. Сложность его алгоритма меньше, меньше 
переменных задействовано, код короче. 
"""