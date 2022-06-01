"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# общая мложность функции O(n log n)
def most_profitable(dict):
    sorted_values = sorted(dict.values(), reverse=True)     # O(n log n)
    sorted_dict = {}                                        # O(1)

    for i in sorted_values[0:3]:                            # O(1)
        for k in dict.keys():                               # O(n)
            if dict[k] == i:                                # O(1)
                sorted_dict[k] = dict[k]                    # O(1)
                break
    return sorted_dict                                      # O(1)


# общая мложность функции O(n log n)
def most_profitable1(dict):
    sorted_dict = {}                                        # O(1)
    sorted_keys = sorted(dict, key=dict.get, reverse=True)  # O(n log n)
    for w in sorted_keys[0:3]:                              # O(1)
        sorted_dict[w] = dict[w]                            # O(1)
    return sorted_dict                                      # O(1)

# из двух функций эффективнее будет вторая, потому как в ней только одна операция со значимой сложностью O(n log n)
# в то время как в первой таких значимых операций две - O(n log n) и O(n)


dict_company = {'Apple': 150000000,
                'Samsung': 100000000,
                'LG': 90000000,
                'Sony': 120000000,
                'Microsoft': 125000000,
                'Intel': 130000000}

print(most_profitable(dict_company))
print(most_profitable1(dict_company))
