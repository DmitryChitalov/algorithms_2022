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

base_company = {
    'yandex': 95135,
    'google': 8412774,
    'adidas': 54485,
    'honor': 445,
    'huawei': 4544,
    'shell': 5485
}


def sorted_1(base):
    lst_from_dict = list(base.items())
    for i in range(len(lst_from_dict)):
        lowest_value = i
        for j in range(i+1,len(lst_from_dict)):
            if lst_from_dict[j][1] > lst_from_dict[lowest_value][1]:
                lowest_value = j
        lst_from_dict[lowest_value], lst_from_dict[i] = lst_from_dict[i], lst_from_dict[lowest_value]
    print(lst_from_dict)


print(sorted_1(base_company))