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


auto_plants = {
    "zig": 1250,
    "zag": 2345,
    "axaxaxa": 7891,
    "lada09": 34567,
    "kiario": 1278,
    "cosmolet": 13472
}


def top_3_company_On(companies):
    # Общая сложность: O(3) + O(3) + O(n) * ( во всех ветвях сложность константная O(1) ) + O(1) = O(n)
    top1, top2, top3 = 0, 0, 0  # O(3)
    name1, name2, name3 = '', '', ''  # O(3)
    for key, val in companies.items():  # O(n)
        if val > top1:  # O(1)
            top3, top2, top1 = top2, top1, val  # O(3)
            name3, name2, name1 = name2, name1, key  # O(3)
        elif val > top2:  # O(1)
            top3, top2 = top2, val  # O(2)
            name3, name2 = name2, key  # O(2)
        elif val > top3:  # O(1)
            top3 = val  # O(1)
            name3 = key  # O(1)

    return [(name1, top1), (name2, top2), (name3, top3)]  # O(1)


def top_3_company_Onlogn(companies):
    # Общая сложность: O(n log n) + O(1) + O(3) * O(1) + O(1) = O(n log n)
    lst = sorted(companies.items(), key=lambda x: x[1], reverse=True)  # O(n log n)
    top3 = []  # O(1)
    for i in range(3):  # O(3)
        top3.append(lst[i])  # O(1)
    return top3  # O(1)


print(top_3_company_On(auto_plants))
print(top_3_company_Onlogn(auto_plants))


# Эффективнее функция top_3_company_Onlogn так как имеет меньшую сложность вычислений
