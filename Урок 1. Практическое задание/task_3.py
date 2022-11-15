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
from random import randint

dictionary_of_companies: dict = {'company_1': randint(100000, 999999),
                                 'company_2': randint(100000, 999999),
                                 'company_3': randint(100000, 999999),
                                 'company_4': randint(100000, 999999),
                                 'company_5': randint(100000, 999999),
                                 'company_6': randint(100000, 999999),
                                 'company_7': randint(100000, 999999),
                                 'company_8': randint(100000, 999999),
                                 'company_9': randint(100000, 999999)
                                 }

print(dictionary_of_companies)

def serch_max_revenue_1(dict_of_company: dict) -> dict:     # O(n)
    ''' Получить словарь компаний с наибольшей прибылью.'''
    tmp_dict: dict = dict_of_company.copy()                 # O(n)
    dict_of_max_revenue_company: dict = dict()              # O(1)
    for _ in range(3):                                      # O(1)
        key: str = max(tmp_dict, key=tmp_dict.get)          # O(n)+O(1)
        value: int = tmp_dict[key]                          # O(1)
        dict_of_max_revenue_company.update({key: value})    # O(1)
        tmp_dict.pop(key)                                   # O(1)
    return dict_of_max_revenue_company                      # O(1)      

def serch_max_revenue_2(dict_of_company: dict) -> dict:                                               # O(n*log(n))
    ''' Получить список трёх компаний с большей прибылью.'''
    tmp_dict: dict = dict_of_company.copy()                                                           # O(n)
    sorted_dict_of_company: list = sorted(dict_of_company.items(), key=lambda x: x[1], reverse=True)  # O(n*log(n))
    result:dict = dict(sorted_dict_of_company[:3])                                                    # O(n)
    return result                                                                                     # O(n)

if __name__ == '__main__':
    print(f'Компании с наибольшей прибылью: {serch_max_revenue_1(dictionary_of_companies)}')
    print(f'Компании с наибольшей прибылью: {serch_max_revenue_2(dictionary_of_companies)}')

# Первое решение быстрее второго, так как во втором много времени тратится на сортировку исходного словаря.
# В первом варианте экономится время за счёт сокращения количества итераций по словарю в цикле for.