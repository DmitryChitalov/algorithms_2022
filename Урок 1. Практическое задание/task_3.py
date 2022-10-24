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

company = {
    'adidas': 12345,
    'puma': 65432,
    'nike': 233456,
    'apple': 1234567890,
    'samsung': 8765443
}


# O(N*logN)
def three_bests_company(company):
    company_list = list(company.items())
    company_list.sort(key=lambda x: x[1], reverse=True)
    for i in range(3):
        print(company_list[i])


# O(N^2)
def three_bests_company2(company):
    company_list = sorted(company.values(), reverse=True)
    for i in range(3):
        for k, v in company.items():
            if v is company_list[i]:
                print(company_list[i], k)



three_bests_company(company)
three_bests_company2(company)




"""
Лучшим вариантом будет первый, т.к. имеет минимальную вычислительную 
сложность
"""