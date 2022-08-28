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

a_sample = {'Prosperity LLC': 1000000,
            'Best Solutions Inc.': 15000000,
            'Comfort Accommodation Ltd': 500000,
            'High Technologies Corp.': 60000000,
            'Too Much Tasty Inc': 40000,
            'Health&Care LLC': 2000000}


# 1 решение. Сложность: O(N log N)
def search_profitable_1(companies_profit):
    most_profitable_3 = []                                        # O(1)
    high_profit_3 = sorted(list(companies_profit.values()))[-3:]  # O(1) + O(N) + O(N log N) + O(1)
    for company, profit in companies_profit.items():              # O(N)
        if profit in high_profit_3:                               # O(1)
            most_profitable_3.append(company)                     # O(1)
    return most_profitable_3                                      # O(1)


# 2 решение. Сложность: O(N^2)
def search_profitable_2(companies_profit):
    most_profitable_3 = []                                  # O(1)
    for num in range(3):                                    # O(1)
        for company, profit in companies_profit.items():    # O(N)
            if profit == max(a_sample.values()):            # O(1) + O(N)
                most_profitable_3.append(company)           # O(1)
                company_max = company                       # O(1)
        del companies_profit[company_max]                   # O(1)
    return most_profitable_3                                # O(1)


print(search_profitable_1(a_sample))
print(search_profitable_2(a_sample))

# Решение 1 эффективнее, т.к. его сложность ниже.
