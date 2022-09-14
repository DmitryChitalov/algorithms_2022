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

company = {'dell': 1500, 'sumsung': 1000, 'yandex': 2000, 'google': 690, 'mail': 13000, 'vk': 6000}


def more_profit_1(data):        # O(n)
    max_profit = []             # O(1)
    new_dct = {}                # O(1)
    for i in data.values():     # O(n)
        max_profit.append(i)
    max_profit = sorted(max_profit)[len(max_profit) - 3:len(max_profit)]
    for num in max_profit:         # O(1)
        for k, v in data.items():  # O(n)
            if v == num:           # O(1)
                new_dct[k] = v     # O(1)
    return new_dct                 # O(1)


print(more_profit_1(company))


def more_profit_2(data):          # O(n**2)
    new_dct = {}                  # O(1)
    key = ''                      # O(1)
    for _ in range(3):            # O(1)
        for k, v in data.items():  # O(n)
            if v == max(data.values()):  # O(n)
                new_dct[k] = v     # O(1)
                key = k            # O(1)
        data.pop(key)             # O(1)
    return new_dct                # O(1)


print(more_profit_2(company))

# Первое решение эффективнее так как сложность линейная
