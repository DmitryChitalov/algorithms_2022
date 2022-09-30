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

companies = {"apple": 3500,
             "google": 2000,
             "yandex": 1500,
             "amazon": 3000,
             "vk": 1900

             }


# Способ 1
# Сложность: O(n^2) — квадратичное время

def search_the_richest(user_dict):
    list_values = sorted(companies.values(), reverse=True)[:3]  # O(n Log n)
    new_dict = {}  # O(1)
    for el in list_values:  # O(n)
        for k, v in companies.items():  # O(n)
            if v == el:  # O(1)
                new_dict[k] = v  # O(1)
    return new_dict  # O(1)


print(search_the_richest(companies))


# Способ 2
# Сложность: O(n*log n) — линейно-логарифмическое время

def search_the_richest_2(user_dict):
    sorted_companies = sorted(companies, key=companies.get, reverse=True)[:3]  # O(n*log n)
    new_dict = {}  # O(1)
    for i in sorted_companies:  # O(1)
        new_dict[i] = companies.get(i)  # O(1)
    return new_dict  # O(1)


print(search_the_richest_2(companies))

'''
Второй способ решения эффективнее, 
т.к. при сложности O(n*log n) с ростом количества элементов время выполнения растет не так быстро, 
как при сложности O(n^2).
'''

