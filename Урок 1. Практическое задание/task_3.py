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


companies_db = {
    'amazon': 200105000,
    'netflix': 9350000,
    'intel': 23006700,
    'facebook': 63890600,
    'walmart': 8104670,
    'sumsung': 6307801,
}

# Сложность O(N log N)
def ranking_1(companies):
    list_from_dict = list(companies.items())                      # O(len(companies))
    list_from_dict.sort()                                         # O(N log N)
    for i in range(3):                                            # O(1)
        print(f"{list_from_dict[i][0]}: {list_from_dict[i][1]}")  # O(1)




# Сложность - O(N)
def ranking_2(companies):
    rank_max = {}                                                  # O(1)
    for i in range(3):                                             # O(1)
        maximum = max(companies.items(), key=lambda k_v: k_v[1])   # O(N)
        del companies[maximum[0]]                                  # O(N)
        rank_max[maximum[0]] = maximum[1]                          # O(1)
    print(rank_max)                                                # O(1)



ranking_1(companies_db)
ranking_2(companies_db)



# Второе решение лучше, так как имеет линейную сложность

