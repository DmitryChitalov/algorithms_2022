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


def companies1(listCompanies):

    topCompany = []                                  # O(len(1))
    
    for i in range(3):                               # O(N)
        company = max(listCompanies.values())        # O(N)
        
        for key, value in listCompanies.items():     # O(N)
            if value == company:                     # O(N)
                topCompany.append(key)               # O(1)
                
                del listCompanies[key]               # O(1)
                
    return topCompany                                # O(1)
    
    
def companies2(listCompanies):

    topCompany = []                                  # O(len(1))
    
    for key1, value1 in listCompanies.items():       # O(N)
        maxi = True                                  # O(1)
        
        for key2, value2 in listCompanies.items():   # O(N)
            if value1 < value2:                      # O(len(n))
                maxi = False                         # O(1)
                
        if maxi:                                     # O(1)
            topCompany.append(key1)                  # O(1)
            
            del listCompanies[key1]                  # O(1)

    return topCompany                                # O(1)
