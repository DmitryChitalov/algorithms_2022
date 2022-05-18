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

# Первая функция выполняется быстрее так как самым сложным алгоритмом, является операция sorted() - O(n log n),
# в отличии от второго способа в котором сложность O(n^2)


def max_profit_1(user_dict):                                            # Сложность: O(n log n)
    sorted_dict = sorted(user_dict, key=user_dict.get, reverse=True)    # O(n log n)
    for i in sorted_dict:                                               # O(n)
        return i, user_dict.get(i)                                      # O(1)


def max_profit_2(user_dict):                        # Сложность: O(n^2)
    for i in range(len(user_dict)):                 # O(n)
        max_value = 0                               # O(1)
        for key, value in user_dict.items():        # O(n)
            if max_value < value:                   # O(1)
                max_value = value                   # O(1)
                key_max_value = key                 # O(1)
    return key_max_value, max_value                 # O(1)


# comp_dict = {'SuperComp': 100, 'MegaComp': 120, 'SuperMegaComp': 80}
#
#
# print(max_profit_1(comp_dict))
# print(max_profit_2(comp_dict))
