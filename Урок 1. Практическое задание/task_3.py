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
#Сложность O(N log N)
def find_year_val1(mp_dict):
    c = []
    if len(mp_dict) > 0:
        d = mp_dict
        a = sorted(list(d.values()))
        b = a[-3:len(a)]
        for key in d.keys():
            if d[key] in b:
                c.append(key)
    return c

def find_year_val2(mp_dict):
    c = []
    a = []
    if len(mp_dict) > 0:
        d = mp_dict
        for i in range(3):
            x = max(d.values())
            for key in d.keys():
                if d[key] == x:
                    c.append(key)
            d.pop(c[i])
    return c

company_val1 = {'comp1': 601, 'comp2': 800, 'comp3': 603, 'comp4': 604, 'comp5': 605, 'comp6': 606, 'comp7': 607 }
print(find_year_val1(company_val1))

company_val2 = {'comp1': 800, 'comp2': 400, 'comp3': 500, 'comp4': 904, 'comp5': 6005, 'comp6': 606, 'comp7': 607 }
print(find_year_val2(company_val2))