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

companies = {
    'Company 1': 100,
    'Company 2': 300,
    'Company 3': 500,
    'Company 4': 700,
    'Company 5': 900,
    'Company 6': 800,
    'Company 7': 600,
    'Company 8': 400,
    'Company 9': 200
}

def top_profit_0(companies): # O(N)
    sorted_companies = {} # O(1)
    for i in range(3):  # O(1)
        max_value = max(companies.items(), key=lambda item: item[1])  # O(N)
        sorted_companies[max_value[0]] = max_value[1] # O(1)
        companies.pop(max_value[0]) # O(1)
    return sorted_companies # O(1)

def top_profit_1(companies): # O(N log N)
    result = {} # O(1)
    top3 = sorted(companies, key=companies.get, reverse=True)[:3] # O(N log N)
    for company in top3: # O(N)
        result[company] = companies[company] # O(1)
    return result # O(1)


# top_profit_0() эффективнее, т.к. выполняет меньше действий с ограниченным количеством итераций.


print(top_profit_0(companies))
print(top_profit_1(companies))