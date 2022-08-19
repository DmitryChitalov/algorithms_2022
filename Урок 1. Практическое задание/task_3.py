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


bd_company = {'Nestle': 1000,  'Mercedes': 634,'Toyota': 200, 'H&M': 650, 'Henkel': 1020, 'Wildberries': 1700,
              'Tomas': 1080, 'Ikea': 7400, 'Ozon': 185}


def max_year_profit_1(dct):  # O(N logN)
    k = []
    v = []
    for key, val in dct.items():  # O(N)
        k.append(key)  # O(1)
        v.append(val)  # O(1)
    data = list(zip(v, k))  # O(N)
    data.sort(reverse=True)  # O(n log n)
    return print(data[:3])  # O(1)


def max_year_profit_2(dct):  # O(n log n) вроде то же самое что max_year_profit_1
    data = sorted(zip(dct.values(), dct.keys()), reverse=True)  # O(n log n)
    return print(data[:3])


def max_year_profit_3(dct):  # O(N^2)
    list_from_dict = list(dct.items())
    for i in range(len(list_from_dict)):  # O(n)
        low_index = i  # O(1)
        for j in range(i + 1, len(list_from_dict)):  # O(N)
            if list_from_dict[j][1] > \
                    list_from_dict[low_index][1]:
                low_index = j  # O(1)
        list_from_dict[i], list_from_dict[low_index] =\
            list_from_dict[low_index], list_from_dict[i]  # O(1)
    print(list_from_dict[:3])  # O(1)


def max_year_profit_4(dct):  # O(n)
    result = {}  # O(1)
    list_d = dict(dct)  # O(1)
    for i in range(3):  # O(3)
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])  # O(n)
        del list_d[maximum[0]]  # O(1)
        result[maximum[0]] = maximum[1]  # O(1)
    print(result)


max_year_profit_1(bd_company)
max_year_profit_2(bd_company)
max_year_profit_3(bd_company)
max_year_profit_4(bd_company)