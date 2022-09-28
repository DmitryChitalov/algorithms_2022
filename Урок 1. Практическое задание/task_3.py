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

company_profit = {
    'aaa' : 100,
    'bbb' : 2000,
    'ccc' : 10000,
    'ddd' : 1000,
    'eee' : 777,
    'fff' : 5000
}

# print(sorted(company_profit.items(), reverse=True, key=lambda comp: comp[1]))
# print(len(company_profit))

# Первый способ. Сложность O(NlogN)
def find_top3_1(company : dict):
    top_3 = {}                                                                      # O(1)
    for k, v in sorted(company.items(), reverse=True, key=lambda comp: comp[1]):    # O(NlogN) - Функция sorted()
        if len(top_3) < 3:                                                          # O(1)
            top_3[k] = v                                                            # O(1)
    print(top_3)                                                                    # O(1)
find_top3_1(company_profit)

# Второй способ. Сложность O(N)
def find_top3_2(company : dict):
    top_3 = {}                                                                      # O(1)
    while len(top_3) < 3:                                                           # O(1)
        max_profit = 0                                                              # O(1)
        max_company = ""                                                            # O(1)
        for k, v in company.items():                                                # O(N)
            if max_profit < v:                                                      # O(1)
                max_profit = v                                                      # O(1)
                max_company = k                                                     # O(1)
        top_3[max_company] = max_profit                                             # O(1)
        del company[max_company]                                                    # O(N)
    print(top_3)                                                                    # O(1)
find_top3_2(company_profit)

# Вывод: Способ 2 быстрее. Т.к. функция sorted() "тяжелая".