#! +
"""
2021-12-18
Geekbrains. Факультет python-разработки
Студент: Папко Роман.
Четверть 1. Алгоритмы и структуры данных на Python. Базовый курс
Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
Домашнее задание 3.
"""
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
companies = {
            'a':round(randint(10**5, 10**7) * 0.01, 2),
            'b':round(randint(10**5, 10**7) * 0.01, 2),
            'c':round(randint(10**5, 10**7) * 0.01, 2),
            'd':round(randint(10**5, 10**7) * 0.01, 2),
            'z':round(randint(10**5, 10**7) * 0.01, 2),
            'k':round(randint(10**5, 10**7) * 0.01, 2),
            'f':round(randint(10**5, 10**7) * 0.01, 2),
            'r':round(randint(10**5, 10**7) * 0.01, 2)
            }
print(companies)

def three_max_sq(dic):  # !!! O(n**2) - Вложенные циклы, квадратичная сложность (
    while len(dic) > 3:
        minimum = min(dic.values())
        for k,v in dic.items():
            if v == minimum:
                remel = k
        del dic[remel]      
    return dic

def three_max_lin(dic):  # !!! O(n) - линейный алгоритм (лучший вариант)
    result = {}
    key_list = list(dic.keys())
    val_list = list(dic.values())
    while len(result) < 3:
        idx_max = val_list.index(max(val_list))
        result[key_list.pop(idx_max)] = val_list.pop(idx_max)
    return result

print(three_max_lin(companies.copy()))
print(three_max_sq(companies.copy()))
