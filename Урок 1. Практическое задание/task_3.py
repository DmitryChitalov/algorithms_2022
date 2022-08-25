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

companies_dict = {
    'GAZPROM': 100000,
    'ROSNEFT': 50000,
    'BAIKALKURORT': 555555,
    'STAVOIL': 5522,
    'BIG BOSS': 15866699,
    'VoVaCo': 9999999,
}

#Решение №1 Сложность: O(n log n) + O(1) + O(n^2)
def top3_v1(dictionary):
    sorted_values = sorted(dictionary.values(), reverse=True)[:3] #O(n log n)
    sorted_dict = {} #O(1)
    for i in sorted_values: #O(n^2)
        for k in dictionary.keys():
            if dictionary[k] == i:
                sorted_dict[k] = dictionary[k]
                break
    print(f'Рэйтинг компаний по прибыли: {sorted_dict}')

top3_v1(companies_dict)

#Решение №2 Сложность: O(1) + O(n log n) + O(n)
def top3_v2(dictionary):
    sorted_dict = {} #O(1)
    sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)[:3] #O(n log n)
    for k in sorted_keys: #O(n)
        sorted_dict[k] = dictionary[k]
    print(f'Рэйтинг компаний по прибыли: {sorted_dict}')

top3_v2(companies_dict)

#Решение №3 Сложность: O(n log n)
def top3_v3(dictionary):
    sorted_tuples = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[:3]
    print(f'Рэйтинг компаний по прибыли: {sorted_tuples}')

top3_v3(companies_dict)

#Решение №3 эффективнее так как его сложность самая низкая O(n log n), а в первом решении есть
# квадратичная сложность O(n^2), а во втором есть ещё O(1) и O(n) помимо O(n log n). Кроме того,
# решение №3 короче и лаконичнее.