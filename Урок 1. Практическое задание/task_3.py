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


def max_three_searcher_v1(dct_in: dict) -> tuple:  # Сложность - O(n * log(n))
    top_3_value_names = tuple(names[0] for names in sorted(dct_in.items(), key=lambda x: x[1])[-3:])
    #  O(1) + O(1) + O(n) + O(n * log(n)) = O(n*log(n))
    return top_3_value_names  # O(1)


def max_three_searcher_v2(dct_in: dict) -> tuple:  # Сложность - O(n^2)
    # O(n) + O(n * log(n)) + O(1) + O(n) * (O(n) * (O(1) + O(1) + O(1))) = O(n) + O(n * log(n)) + O(n^2) = O(n^2)
    dct_in_copy = dct_in.copy()  # O(n)
    sorted_dct_values = sorted(list(dct_in_copy.values()))  # O(n*log(n))
    three_max_val_name = list()  # O(1)
    for i in sorted_dct_values[-3:]:  # O(n) + O(1) = O(n)
        for key in dct_in_copy.keys():  # O(n)
            if dct_in_copy[key] == i:  # O(1)
                three_max_val_name.append(key)  # O(1)
                dct_in_copy.pop(key)  # O(1)
                break
    return tuple(three_max_val_name)  # O(1)


if __name__ == '__main__':
    data_dict = {
        'name_1': 3000,
        'name_2': 1000,
        'name_3': 1000,
        'name_4': 8000,
        'name_5': 800,
        'name_6': 11000
    }
    print(f'Поиск трёх максимально прибыльных компаний v1: {max_three_searcher_v1(data_dict)}')
    print(f'Поиск трёх максимально прибыльных компаний v2: {max_three_searcher_v2(data_dict)}')

'''
Решение N 1 является более удачным, т.к. обходит значения из словаря на 1 раз меньше (2 против 3 у второго решения),
не требует копирования входящих данных.
'''