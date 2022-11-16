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

# 1 Способ. Cложность: O(n log n)

def find_top_3_1(dict):
    sorted_company = (sorted(dict.items(), key=lambda item: item[1], reverse=False))[-3:]    # O(n log n)
    return sorted_company   # O(1)

# 2 Способ. Cложность: O(n**2)

def fint_top_3_2(dict):                                # O(n**2)
    sorted_company = sorted(dict.values())[-3:]        # O(n log n)
    new_sorted_company = {}                            # O(1)
    for i in sorted_company:                           # O(n)
        for k in dict.keys():                          # O(n)
            if dict[k] == i:                           # O(1)
                new_sorted_company[k] = dict[k]        # O(1)
    return new_sorted_company                          # O(1)


dict = {
    'Company_1': 12345,
    'Company_2': 678,
    'Company_3': 22222,
    'Company_4': 9999,
    'Company_5': 3,
    'Company_6': 2,
    'Company_7': 1,
    'Company_8': 1212121,
}

print(find_top_3_1(dict))
print(fint_top_3_2 (dict))