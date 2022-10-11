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


def eat_the_rich_1(dct):
    """
    итоговая сложность: O(N logN) = O(N) + O(N logN) + O(1) + O(N) * O(1) * O(1) + O(1)
    """
    dct_values = list(dct.values())         # O(N)
    dct_values.sort()                       # O(N logN)
    richest_companies = {}                  # O(1)
    for key, value in dct.items():          # O(N)
        if value in dct_values[-3:]:        # O(1)
            richest_companies[key] = value  # O(1)
    return richest_companies                # O(1)


def eat_the_rich_2(dct):
    """
     итоговая сложность: O(N)
    """
    richest_companies = {}                              # O(1)
    dct_copy = dct.copy()                               # O(N)
    for _ in range(3):                                  # O(1)
        richest = max(dct_copy.items())                 # O(N)
        dct_copy.pop(richest[0])                        # O(1)
        richest_companies[richest[0]] = richest[1]      # O(1)
    return richest_companies                            # O(1)

# вывод: второе решение быстрее если судить по Big O notation,
# но на практике в большинстве случаев первое отрабатывает быстрее


if __name__ == '__main__':
    from time import perf_counter
    companies = {'1_company': 1000, '4_company': 4000, '2_company': 2000, '5_company': 5000, '3_company': 3000}
    start = perf_counter()
    print(eat_the_rich_1(companies), (perf_counter() - start))
    start2 = perf_counter()
    print(eat_the_rich_2(companies), (perf_counter() - start2))
