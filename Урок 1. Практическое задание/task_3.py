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

from random import randint


# 1
def search_one(company):
    company_list = list(company.items())  # O(n)
    company_list.sort(key=lambda val: val[1], reverse=True)  # O(n*log n)
    for val in range(3):  # O(1)
        return dict(company_list[0:3])


# Итоговая сложность O(n*log n)


# 2
def search_two(company):
    company_list = list(company.items())  # O(n)
    for val in range(3):  # O(1)
        for j in range(val + 1, len(company_list)):  # O(n)
            if company_list[j][1] > company_list[val][1]:  # O(1)
                company_list[j], company_list[val] = company_list[val], company_list[j]  # O(1)
    return dict(company_list[0:3])  # O(1)


# Итоговая сложность O(n)
# Первая задача будет медленнее так как по сложности O(n*log n)>O(n)

# Формируем словарь компаний и выручек
d_company = {f'comp_{randint(0, 10)}': randint(100, 15000) for val in range(randint(3, 15))}

print(f'{search_one(d_company)=}')
print(f'{search_two(d_company)=}')
