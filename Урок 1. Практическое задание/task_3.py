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
company1 = {"Beeline": 123456789, "MTS": 321654987, "Rostelecom": 213546879, "Skynet": 753159864, "Megafon": 754896123,
            "Tele2": 159357456}

# Первый алгоритм - O(n**2)


def find_max(com_dict):
    lst_com_dict = list(com_dict.items())  # O(1)
    for i in range(len(lst_com_dict)):  # O(n)
        max_key = i  # O(1)
        for j in range(i+1, len(lst_com_dict)):  # O(n)
            if lst_com_dict[j][1] > lst_com_dict[max_key][1]:  # O(1)
                max_key = j  # O(1)
        lst_com_dict[i], lst_com_dict[max_key] = lst_com_dict[max_key], lst_com_dict[i]  # O(1)
    return dict(lst_com_dict[:3])  # O(n)


print(find_max(company1))

# Второй алгоритм O(n log n) - эффективнее, т.к. выполняется меньшее количество операций


def find_max2(com_dict):
    sorted_companies = sorted(com_dict.items(), key=lambda x: x[1], reverse=True)  # O(n log n)
    return dict(sorted_companies[:3])  # O(n)


print(find_max2(company1))


