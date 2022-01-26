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

company = {
    'BMW': 4500000,
    'LADA': 300000,
    'Jeep': 3400000,
    'Toyota': 4300000,
    'Volkswagen': 3800000
}

# 1     Сложность: О(NlogN) - Линейно-логарифмитическая

lst_dic = list(company.items())                    # O(N)
lst_dic.sort(key=lambda i: i[1], reverse=True)     # O(NlogN)
for i in range(3):                                 # O(1)
    print(lst_dic[i][0], ':', lst_dic[i][1])       # O(1)


# 2     Сложность: O(N) - Линейная

def profit_max_3(company):
    input_max = {}                                              # O(1)
    lst_d = dict(company)                                       # O(N)
    for j in range(3):                                          # O(1)
        maximum = max(lst_d.items(), key=lambda c: c[1])        # O(N)
        del lst_d[maximum[0]]                                   # O(N)
        input_max[maximum[0]] = maximum[1]                      # O(1)
    return input_max                                            # O(1)


print(profit_max_3(company))                                   # O(N)



# Вывод: Вариант 2 будет являться наиболее эффективным так как затратится меньше времени.