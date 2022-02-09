"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
werwer
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

COMPANY_INCOME = {
    'Company_1': 100000,
    'Company_2': 120000,
    'Company_3': 25000,
    'Company_4': 250000,
    'Company_5': 750000,
    'Company_6': 450000,
    'Company_7': 30000
}

# Решение 1 O(NlogN)
def get_profit_1(dictionary: dict):
    res = []  # O(1)
    for i in dictionary.items():  # O(n)
        res.append(i)  # O(1)
    res.sort(key=lambda x: (x[1], x[0]), reverse=True)  # O(NlogN)
    return res[0:3]

print(get_profit_1(COMPANY_INCOME))


# Решение 2   O(N^2)
def get_profit_2(dictionary: dict):
    max_values = {}  # O(1)
    for i in dictionary.keys():  # O(N)
        max_ = dictionary.get(i)  # O(1)
        for j in dictionary.keys():  # O(N)
            if max_ < dictionary.get(j):  # O(1)

                max_ = dictionary.get(i)  # O(1)
            max_values[i] = max_  # O(1)
    return list(sorted(max_values.items(), key=lambda v: v[1], reverse=True))[:3]  # O(1)
print(get_profit_2(COMPANY_INCOME))