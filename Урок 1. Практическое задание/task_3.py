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

info_store = {
    "poor company": -345.414,
    "negative solutions": -31412515141412,
    "Google vilage": 1324155.3130,
    "Abb": 43431211,
    "Siemens": 116002334.44,
    "Reaktor base": 2030304,
    "Kumara": 5922323.4214,
    "Drama company": 323330314,
    "Komedy Film": 203204124.31,
    "Some other": 12034
}


def get_three_profitable_comp(info_storage:  dict) -> dict:
    """
    Первый вариант.
    :arg = dict possible also (tuple, list)
    :return dict

    Сложность: Т(n) = 2n + 5 => O(n)
    """
    tmp_storage = info_storage.copy()                                           # O(n)
    max_annual_profit_companies = {}                                            # O(1)
    for x in range(3):                                                          # O(1)
        company, value = max(tmp_storage.items(), key=lambda x: x[1])           # O(n)
        del tmp_storage[company]                                                # O(1)
        max_annual_profit_companies.update({company: value})                    # O(1)
    return max_annual_profit_companies                                          # O(1)


print(f"Вариант 1: {get_three_profitable_comp(info_store)}")

def get_three_profitable_comp_2(info_storage:  dict) -> dict:
    """
    второй вариант.
    :arg = dict possible also (tuple, list)
    :return dict

    Сложность: T(n) = n^2 + n log n + 2 = O(n^2)
    """
    tmp_storage = [(company, profit) for company, profit in info_storage.copy().items()]     # O(n^2)
    tmp_storage.sort(key=lambda x: x[1])                                                     # O(nlog n)
    max_annual_profit_companies = {company: profit for company, profit in tmp_storage[-3:]}  # O(1)
    return max_annual_profit_companies                                                       # O(1)

print(f"Вариант 2: {get_three_profitable_comp_2(info_store)}")


"""
Решение 1 более еффективно, так как сложность O(n)
Решение 2 более компактно но сложность квадратичная
"""