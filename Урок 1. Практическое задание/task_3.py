"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
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

""" 
Первый и наверное самый замудрённый
вариант выполнения алгоритма 
СЛОЖНОСТЬ - O(n)
"""
companies = {'Apple': 1000000, 'Microsoft': 12381173, 'Disney': 12378389, 'Sony': 384593, '20th century fox': 35934723}  #O(1)
temp_companies = companies.copy()  #O(n)
top_companies = {}  #O(1)
for i in range(3):  #O(1)
    max_income = max(temp_companies.values()) #O(n)
    # max(temp_companies.values())
    top_companies[list(temp_companies)[list(temp_companies.values()).index(max_income)]] = max_income  #O(1)
    del temp_companies[list(temp_companies)[list(temp_companies.values()).index(max_income)]]  #O(n)

# print(max(companies.values()), list(companies)[list(companies.values()).index(35934723)], list(companies.values()).index(35934723), type(companies))

print(top_companies)
"""
end
"""

""" 
Второй чуть получше 
СЛОЖНОСТЬ - O(n log n)
"""

companies = {'Apple': 1000000, 'Microsoft': 12381173, 'Disney': 12378389, 'Sony': 384593, '20th century fox': 35934723} #O(1)
sort_companies = sorted(companies.values(), reverse=True)  #O(n log n)
print(sort_companies)
n = 0  #O(1)
for i in sort_companies:  #O(n)
    n += 1 #O(1)
    name = list(companies)[list(companies.values()).index(i)] #O(n)
    print(name, companies[name])
    if n == 3: #O(1)
        break
