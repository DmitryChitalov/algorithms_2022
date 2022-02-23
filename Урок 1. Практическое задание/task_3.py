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
base_comp = {
    "yandex": 2000,
    "gazpron": 500,
    "microsoft": 2300,
    "perecrestok": 5400,
    "rosnano": 10,
    "appel": 2000,
    "biocad": 4030,
    "apteka": 299,
    "hiomi": 569,
    "adidas": 4313,
    "acron": 6703
}

#O(n^2)
def sorted_1(base_comp):
    list_from_dict = list(base_comp.items())
    for i in range(len(list_from_dict)):
        lowest_val_idx = 1
        for j in range(i + 1, len(list_from_dict)):
            if list_from_dict[j][1] > list_from_dict[lowest_val_idx][1]:
                lowest_val_idx = j
        list_from_dict[i], list_from_dict[lowest_val_idx] = list_from_dict[lowest_val_idx], list_from_dict[i]
    print(list_from_dict[0:3])


# O(n log n)
def sorted_2(base_comp):
    list_from_dict = list(base_comp.items())
    list_from_dict.sort(key=lambda i: i[1], reverse=True)
    for i in range(3):
        print(f'{list_from_dict[i][0]}: {list_from_dict[i][1]}')
