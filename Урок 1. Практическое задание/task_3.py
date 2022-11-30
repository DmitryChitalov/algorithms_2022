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
from collections import Counter

# Сложность - O(n)
count = Counter(profit_statement)
highest_value = count.most_common(3) # O(n log n)
for i in highest_value:     # O(n)
    print(i[0], '-',i[1])


# Сложность - О(n^2)
list_d = list(profit_statement.values())    # O(k) + O(1)
profit_dict = dict()    # O(len(...))
list_d.sort(reverse=True)   # O(n log n)
list_d = list_d[:3]     # O(1)
for i in list_d:        # O(n)
    for el in profit_statement.keys():      # O(n) + O(1)
        if (profit_statement[el] == i):     # O(1)
            print(str(el) + " : " + str(profit_statement[el]))


profit_statement = {'margiela': 123456,
                    'balmain': 456789,
                    'mcqueen': 789456,
                    'bluemarine': 951753,
                    'offwhite': 753951,
                    'casadei': 852741,
                    'moncler': 963852}

# Лучший вариант - 1-й (O(n)), так как обладает меньшей сложностью.