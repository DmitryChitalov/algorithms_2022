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
def get_3_best_comp_1(comp_dict):   # O(n log n)
    sorted_company_inf = (sorted(company_inf.items(), key=lambda item: item[1]))[-3:]    # O(n log n)
    return sorted_company_inf   # O(1)


def get_3_best_comp_2(comp_dict):   # O(n**2)
    sorted_values = sorted(comp_dict.values())[-3:] # O(n log n)
    new_sorted_dict = {}                            # O(1)
    for i in sorted_values:                         # O(n)
        for k in comp_dict.keys():                  # O(n)
            if comp_dict[k] == i:                   # O(1)
                new_sorted_dict[k] = comp_dict[k]   # O(1)
    return new_sorted_dict                          # O(1)

# get_3_best_comp_1 (O(n log n)) эффективнее чем get_3_best_comp_2 (O(n**2))

if __name__ == '__main__':
    company_inf = {
        "company_1": 10000,
        "company_2": 15000,
        "company_3": 1000,
        "company_4": 100000,
        "company_5": 17000,
        "company_6": 30000,
        "company_7": 50000,
        "company_8": 70000
    }

    print(company_inf)
    print(get_3_best_comp_1(company_inf))
    print(get_3_best_comp_2(company_inf))