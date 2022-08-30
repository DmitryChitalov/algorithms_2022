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

company_info = {
    'company_name1': 100,
    'company_name2': 120,
    'company_name3': 1000,
    'company_name4': 111,
    'company_name5': 402,
    'company_name6': 579,
    'company_name7': 321,
    'company_name8': 2000,
    'company_name9': 10,
    'company_name10': 392
}


# O(N logN)
def sort_company_1(company_info):
    sorted_tuple = sorted(company_info.items(), key=lambda x: x[1], reverse=True)
    biggest_companys = [sorted_tuple[0], sorted_tuple[1], sorted_tuple[2]]
    dict(biggest_companys)
    return biggest_companys


# O(N^2)
def sort_company_2(company_info):
    list_company = list(company_info.items())
    for i in range(len(list_company)):
        min_val_index = i
        for j in range(i + 1, len(list_company)):
            if list_company[j][1] > list_company[min_val_index][1]:
                min_val_index = j
            list_company[i], list_company[min_val_index] = list_company[min_val_index], list_company[i]
    return list_company[0:3]

print(sort_company_1(company_info))
print(sort_company_2(company_info))