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

company = {
    'ООО "Рога и копыта"': 10000,
    'ООО "Фарма фирма"': 14000,
    'ООО "Ко и компания"': 9000,
    'ООО "Мастер и Марго-Рита"': 6500,
    'ООО "Сибиряки': 17300}


def top3_company_v1(dict):                  # O( n log n) или O(n**4) так и не понял как суммировать
    top3_company = {}                       # O(1)
    dict_list = list(dict.values())         # O(n)
    dict_list.sort(reverse=True)            # O( n log n)
    for el in dict_list[:3]:                # O(n)
        for name, prof in dict.items():     # O(n)
            if prof == el:                  # O(n)
                top3_company[name] = prof   # O(1)
    return top3_company                     # O(1)


def top3_company_v2(dict):                                      # O(n)
    top3_company = {}                                           # O(1)
    for x in range(3):                                          # O(1)
        company, money = max(dict.items(), key=lambda x: x[1])  # O(n)
        del dict[company]                                       # O(1)
        top3_company.update({company: money})                   # O(1)
    return top3_company                                         # O(1)


print(top3_company_v1(company))
print(top3_company_v2(company))

# Наилучший вариант top3_company_v2 так как затрачивает меньше ресурсов
