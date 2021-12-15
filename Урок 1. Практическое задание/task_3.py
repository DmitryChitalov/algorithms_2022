"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

companies = {
    'MailRU': 23103,
    'Google': 133904823098420984098,
    'Rambler': 384270,
    'Apple': 48279872047093849,
    'Huawei': 475984759485987987
}


def find_richest_companies_1(companies, n):
    return sorted(companies, key=companies.get, reverse=True)[:n]


print(find_richest_companies_1(companies, 3))

# T(n) = n log n + n + n
# O(n log n)
# данное решение эффективнее (линейно-логарифмическая сложность
# + само решение намного короче)


def find_richest_companies_2(companies, n):
    values = list(companies.values())
    for i in range(len(values)):
        smallest_number = i
        for j in range(i + 1, len(values)):
            if values[j] > values[smallest_number]:
                smallest_number = j
        values[i], values[smallest_number] = values[smallest_number], values[i]
    richiest = []
    count = 0
    while count < n:
        for k, v in companies.items():
            if v == values[count]:
                richiest.append(k)
                count += 1
    return(richiest)


print(find_richest_companies_2(companies, 3))

# T(n) = 1 + 2n^2 + 1 + 1 + n^2 + 1 = 3 + 2n^2 + n^2
# O(n^2)