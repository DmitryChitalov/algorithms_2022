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

companies = {
    'Abernathy, Goyette and Lehner': 7888509,
    'Champlin & Sons': 7888509,
    'Durgan LLC': 7888509,
    'Hand-Lebsack': 9836273,
    'Kub Group': 4176255,
    'Labadie Ltd': 6562167
            }


def three_max_earnings_1(dct):                                                         # O(nlogn)
    sorted_tuples = sorted(dct.items(), key=lambda item: item[1], reverse=True)[:3]    # O(nlogn)
    sorted_dct = {k: v for k, v in sorted_tuples}                                      # O(n)
    return sorted_dct                                                                  # O(1)


def three_max_earnings_2(dct):                            # O(n^2)
    sorted_dct = {}                                       # O(1)
    sorted_values = sorted(dct.values(), reverse=True)    # O(nlogn)
    for j in sorted_values:                               # O(n)
        if len(sorted_dct) == 3:                          # O(1)
            break                                         # O(1)
        for k in dct.keys():                              # O(n)
            if dct[k] == j and k not in sorted_dct:       # O(1)
                sorted_dct[k] = dct[k]                    # O(1)
                break                                     # O(1)
    return sorted_dct                                     # O(1)


print(three_max_earnings_1(companies))
print(three_max_earnings_2(companies))

# Эффективнее решение 1 (функция three_max_earnings_1),
# т.к. оно выполняется за линейно-логарифмическое время (nlogn),
# в отличие от решения 2, которое выполняется за квадратичное время (n^2).
