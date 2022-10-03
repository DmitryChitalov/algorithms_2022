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

companies = {'ARS': 526879.45, 'SELECT': 895674.32, 'FOX': 789456.78, 'mail-group': 478956.56, 'MSI': 478955.55}

# 1 способ
list_values = sorted(list(companies.values()), reverse=True)[:3]                     # O(n)
for el in list_values:                                                               # O(1)
    for k, v in companies.items():                                                   # O(n)
        if v == el:                                                                  # O(n)
            print(k, ':', v)                                                         # O(1)


# O(n)  + O(1) + O(n)  + O(1) = O(n)

# 2 способ
sorted_companies = sorted(companies, key=companies.get, reverse=True)[:3]    # O(n*log n)
for i in sorted_companies:                                                   # O(n)
    print(i, ':', companies.get(i))                                          # O(1)

# O(n*log n) + O(1) + O(1) = O (n *log n)

# 3 способ
companies_out = {k: v for k, v in sorted(companies.items(), key=lambda item: item[1])} # O(n log n)
list_key = []                                                                          # O(1)
list_val = []                                                                          # O(1)
max_profit = 0                                                                         # O(1)
for k, v in companies_out.items():                                                      # O(n)
    list_val.append(v)                                                                  # O(n)
    list_key.append(k)                                                                  # O(n)

for i in range(3):                                                                      # O(n)
    if i == 0:                                                                          # O(1)
        print(f'{list_key[-1:]} : {list_val[-1:]}')                                     # O(1)
    else:
        print(f'{list_key[-1-i:-i]} : {list_val[-1-i:-i]}')                             # O(1)

O(n*log n) + 6 * O(1) + 3 * O(n) = O(n)


# Эффективнее 2 способ, т.к. он лаконичнее и итоговая сложность O(n * log n) меньше, чем O(n).
# 3 способ самый неудачный нагородил то что мог -))).
# Используйте встроенные функции.