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

profit_company = {'Apple': 10000, 'Yandex': 1000, 'Google': 8000, 'Microsoft': 9000, 'IBM': 3000}


def by_value(item):
    return item[1]                                                          # O(1)


max_profit = {}                                                             # O(1)
i = 0                                                                       # O(1)
for k, v in sorted(profit_company.items(), key=by_value, reverse=True):     # O(n + n log n) или # O(n + n log n)
    if i < 3:                                                               # O(1)
        max_profit.setdefault(k, v)                                         # O(1)
    i = i + 1                                                               # O(1)
print("copy_past", max_profit)                                              # O(1)

# Первый способ:
def answer_first(dictionary, count=3):
    sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])} # O(1 + n + n log n)
    result = {}
    i = 0
    while i < count:
        tmp_lst = list(sorted_dict.popitem())
        result[tmp_lst[0]] = tmp_lst[1]
        i += 1
    return result


# Второй способ:
def answer_two(company):
    sorted_values = sorted(company.values(), reverse=True)  # O(n log n)
    sorted_dict = {}                                        # O(1)
    for i in range(3):                                      # O(1)
        for k in company.keys():                            # O(n)
            if company[k] == sorted_values[i]:              # O(1)
                sorted_dict[k] = company[k]                 # O(1)
                break
    return sorted_dict


print("answer_first", answer_first(profit_company))
print("answer_two", answer_two(profit_company))

"""
Второй вариант предпочтительнее так как используется цикл for, а для перебора элементов он работает быстрее чем while
"""