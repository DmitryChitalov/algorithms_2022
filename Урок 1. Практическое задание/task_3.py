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
companies = {'Лукойл': 7841, 'Норильский никель': 877, 'Магнит': 1368, 'Новатэк': 862, 'Сургутнефтегаз': 1814,
             'Evraz': 770, 'Татнефть': 932, 'X5 Group': 1734}

# Первый вариант. Линейная-логарифмическая сложность O(n log n).

biggest_company = sorted(list(companies.values()), reverse=True)[:3]  # O(n log n)
for i in biggest_company:  # O(n)
    for k, v in companies.items():  # O(n)
        if v == i:  # O(1)
            print(k, ':', v)  # O(1)


# Второй вариант. Квадратичная сложность O(n^2).

def biggest_company_2(company):
    list_company = list(company.items())
    for a in range(len(list_company)):  # O(n)
        smallest_index = a  # O(1)
        for b in range(a + 1, len(list_company)):  # O(n)
            if list_company[b][1] > list_company[smallest_index][1]:  # O(1)
                smallest_index = b  # O(1)
        list_company[a], list_company[smallest_index] = list_company[smallest_index], list_company[a] # O(1)
    print(list_company[0:3])  # O(1)


print(biggest_company_2(companies))

# Чем меньше сложность, тем эффективнее решение. В данном случае второй вариант эффективнее.