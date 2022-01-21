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
companies = {"Firm1": 100000, "Firm2": 140000, "Firm3": 90000, "Firm4": 120000, "Firm5": 50000}

companieslist = list(companies.items())
companieslist.sort(key=lambda k: k[1], reverse=True)
for i in range(3):
    if len(companieslist) > i:
        print(companieslist[i][0], ':', companieslist[i][1])

print(f'-'*20)

for i in range(3):
    _max = 0
    _max_key = ''
    for company in companies:
        if companies[company] > _max:
            _max = companies[company]
            _max_key = company
    print(_max_key, companies.pop(_max_key))
    if len(companies) == 0:
        break

