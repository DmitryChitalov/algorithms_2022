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


companies = {'Toyota':150000,'Nissan':200000,'Honda':175000,'Suzuki':190000,'Lexus':250000}

# Cложность - O(n**2)
def max_profit_1(data):
    sorted_values = sorted(data.values(),reverse=True)
    sorted_dict = {}

    for i in sorted_values:
        for k in data.keys():
            if data[k] == i:
                sorted_dict[k] = data[k]
                if len(sorted_dict) == 3:
                    return sorted_dict


print(max_profit(companies))

# Сложность O(n log n)
def by_value(data):
    return data[1]


max_profit = {}
i = 0
for k, v in sorted(companies.items(), key=by_value, reverse=True):
    if i < 3:
        max_profit.setdefault(k, v)
    i = i + 1
print(max_profit)


