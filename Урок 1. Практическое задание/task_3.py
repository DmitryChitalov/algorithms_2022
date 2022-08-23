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
import csv

companies = ['samsung', 'apple', 'xiaomi', 'nokia', 'huawei']
revenues = [100500, 100000, 90000, 50000,
            75000]  # элемент под номером i в списке компаний соответствует элементу с тем же номером в списке прибылей
max_comp_list = []
max_rev_list = []


def best_three_1(companies, revenues):  # O(n)
    for i in range(3):  # O(1)
        max_rev = revenues[1]  # O(1)
        for company in companies:  # O(n)
            if revenues[companies.index(company)] > max_rev:  # O(1)
                max_rev = revenues[companies.index(company)]  # O(1)
        max_rev_list.append(max_rev)  # O(1)
        max_comp_list.append(companies[revenues.index(max_rev)])  # O(n)
        companies.pop(revenues.index(max_rev))  # O(n)
        revenues.remove(max_rev)  # O(n)
    for el in max_comp_list:  # O(n)
        companies.append(el)  # O(1)
    for el in max_rev_list:  # O(n)
        revenues.append(el)  # O(1)
    return max_comp_list, max_rev_list  # O(1)


print(best_three_1(companies, revenues))

companies_dict = dict(zip(companies, revenues))  # теперь компании в виде словаря вида компания: прибыль


def get_key(d, value):  # O(n**2)
    for k, v in d.items():  # O(n**2)
        if v == value:  # O(1)
            return k  # O(1)


def best_three_2(companies_dict):  # O(n**2)
    max_rev = list(companies_dict.values())[0]  # O(1)
    max_rev_2 = list(companies_dict.values())[0]  # O(1)
    max_rev_3 = list(companies_dict.values())[0]  # O(1)
    for revenue in list(companies_dict.values()):  # O(n)
        if revenue > max_rev:  # O(1)
            max_rev = revenue  # O(1)
    for revenue_2 in list(companies_dict.values()):  # O(n)
        if revenue_2 != max_rev and revenue_2 > max_rev_2 or max_rev_2 == max_rev:  # O(1)
            max_rev_2 = revenue_2  # O(1)
    for revenue_3 in list(companies_dict.values()):  # O(n)
        if revenue_3 != max_rev and revenue_3 != max_rev_2 and revenue_3 > max_rev_3 or max_rev_3 == max_rev or max_rev_3 == max_rev_2:  # O(1)
            max_rev_3 = revenue_3  # O(1)
    best_three = {get_key(companies_dict, max_rev): max_rev, get_key(companies_dict, max_rev_2): max_rev_2,
                  get_key(companies_dict, max_rev_3): max_rev_3}  # O(n**2)
    return best_three  # O(1)


print(best_three_2(companies_dict))  # у второго метода сложность O(n**2) только из-за метода get_key, лол


def best_three_3():  # O(n**3) из-за способа записи результата
    with open('companies.csv', 'r') as file:  # O(1) ???
        res = []  # O(1)
        read = list(csv.reader(file))  # O(1)
        for i in read:  # O(n)
            max = int(i[1])  # O(1)
            for j in read:  # O(n)
                if int(j[1]) > max:  # O(1)
                    max = int(j[1])  # O(1)
            for k in read:  # O(n)
                if int(k[1]) == max:  # O(1)
                    res.append(k)  # O(1)
                    read.remove(k)  # O(n)
        file.close()  # O(1)
    return res[:3]  # O(1)


print(best_three_3())
# Первый способ имеет самую низкую сложность, и потому является самым эффективным