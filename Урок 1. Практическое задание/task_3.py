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


""" Решение №1"""

def max_profit(comp):

    best_corp = []

    def max_val(lst):
        """Сложность данной функции О(n^2)"""
        max_value = 0
        """Сложность данной функции О(n^2)"""
        for i in lst: # O(n)
            for val in i.values(): # O(n)
                if type(val) is int and val > max_value: #O(1)
                    max_value = val #O(1)
        """Сложность данной функции О(n^2)"""
        for i in lst: # O(n)
            for val in i.values(): # O(n)
                if val == max_value: # O(1)
                    best_corp.append(i) # O(1)
                    lst.remove(i) # O(n)
        return max_value
        """Сложность всей функции О(n^2)"""

    """Этим выражение мы запускаем 3 раза выражение сложностью O(n^2)"""
    while len(best_corp) < 3:
        max_val(comp)

    return best_corp


company_profit = [{
            'company': 'lg',
            'annual_profit': 10000000
           },
            {
            'company': 'boss',
            'annual_profit': 20000000
            },
            {
            'company': 'samsung',
            'annual_profit': 50000000
            },
            {
            'company': 'Huawei',
            'annual_profit': 70000000
            },
            {
            'company': 'obi',
            'annual_profit': 13000000
           },
            {
            'company': 'rost',
            'annual_profit': 23000000
            },
            {
            'company': 'spaceX',
            'annual_profit': 55000000
            },
            {
            'company': 'Xiaomi',
            'annual_profit': 77000000
            }
            ]

# print('Три компании с самой большой прибылью:', max_profit(company_profit))


""" Решение №2 """


def max_profit_2(lst):

    best_corp = []

    def max_val(company):
        max_profit = 0
        for i in company:
            if i["annual_profit"] > max_profit:
                max_profit = i["annual_profit"]

        for i in company:
            if i["annual_profit"] == max_profit:
                best_corp.append(i["company"])
                company.remove(i)
        return max_profit

    while len(best_corp) < 3:
        max_val(lst)

    return best_corp

print('Три компании с самой большой прибылью:', max_profit_2(company_profit))
