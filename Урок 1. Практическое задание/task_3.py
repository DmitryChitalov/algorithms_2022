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


def top_3_company_0(company_dict, top_3_list=[]):
    """
    Функция принимает словарь и возвращает три значения с наибольшим ключом.
    Сложность: O(n**2)
    Данное решение более эффективное чем top_3_company_1(), т.к. имеет меньшую сложность и, как следствие,
    выполняется быстрее. Хоть и медленнее чем при использовании heapq.nlargest()
    """
    company_profit_sorted = sorted(company_dict, reverse=True)  # O(n log n)
    for profit in company_profit_sorted:  # O(n)
        for value, company_name in company_dict.items():  # O(n)
            if profit == value and len(top_3_list) != 3:  # O(1)
                top_3_list.append(company_name)  # O(1)

    return top_3_list  # O(1)


def top_3_company_1(company_dict, top_3_list=[]):
    """
    Функция принимает словарь и возвращает три значения с наибольшим ключом.
    Сложность O(n**3)
    """
    company_list = list(company_dict)
    while len(top_3_list) != 3:  # O(1)
        for profit in company_list:  # O(n)
            if profit == max(company_list):  # O(n)
                top_3_list.append(company_dict.get(profit))  # O(1)
                company_list.remove(profit)  # O(n)

    return top_3_list  # O(1)


if __name__ == '__main__':
    company_2021 = \
        {57411: 'Apple',
         49287: 'Saudi Aramco',
         47053: 'SoftBank Group',
         47050: 'Microsoft',
         10269: 'Alphabet',
         29146: 'Facebook'}

    print(top_3_company_0(company_2021))
    print(top_3_company_1(company_2021))
