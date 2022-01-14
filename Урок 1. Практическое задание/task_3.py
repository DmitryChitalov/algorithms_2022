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

company_profit = {
    'apple': 100,
    'alphabet': 90,
    'ooo kasimov': 2,
    'шиномонтаж у Петра': 10,
    'tesla': 10,
    'bp': 50,
    'sber': 30
}

# best_three1 ==> O(n)
# Самый быстрый вариант, так как по сути находим выборку за один проход по основной коллекции
def best_three1(company_profit, comp_num=3): # O(1) сложность пишем с учетом что comp_num не меняется
    if len(company_profit) <= comp_num: # O(1)
        return [company for company in company_profit.keys()] # O(n)

    inner_company_profit = company_profit.copy()
    best_companies = [] # O(1)
    best_profits = [] # O(1)
    for _ in range(comp_num): # O(1)
        cur_company, cur_profit = inner_company_profit.popitem() # O(1)
        best_companies.append(cur_company) # O(1)
        best_profits.append(cur_profit) # O(1)


    for cur_company, cur_profit in inner_company_profit.items(): # O(n)
        # Найдем компанию (кандидат на вылет) с минимальной прибылью в сборке лучших 
        best_min_profit, best_num_company_with_min_profit = best_profits[0], 0 # O(1)
        for num in range(1, comp_num): # O(1)
            if best_min_profit > best_profits[num]: # O(1)
                best_min_profit = best_profits[num] # O(1)
                best_num_company_with_min_profit = num # O(1)
        if cur_profit > best_min_profit: # O(1)
            best_companies[best_num_company_with_min_profit] = cur_company # O(1)
            best_profits[best_num_company_with_min_profit] = cur_profit # O(1)
    return best_companies # O(1)   

# best_three2 ==> O(nlogn)
# Не сильно хуже в скорости в сравнении с первым вариантом. До 1000 компаний разницы нет, 
# при 1000000 компаний первый способ работает в 5 раз быстрее. 
# Однако он простой в реализации и понимании.
def best_three2(company_profit, comp_num=3): # O(1) сложность пишем с учетом что comp_num не меняется
    inner_company_profit = list(company_profit.items()) #O(n)
    inner_company_profit.sort(key=lambda c_p: c_p[1]) #O(nlogn)
    best_companies = [comp[0] for comp in inner_company_profit[-comp_num:]] #O(1)
    return best_companies #O(1)

# best_three3 ==> O(n^2)
# Худший варинт. Но если компаний не много, можно использовать.
def best_three3(company_profit, comp_num=3): # O(1) сложность пишем с учетом что comp_num не меняется
    companies = list(company_profit.keys()) # O(n)
    profits = list(company_profit.values()) # O(n)

    for i1 in range(len(companies)): # O(n)
        for i2 in range(i1+1, len(companies)): # O(n)
            if profits[i1] > profits[i2]: # O(1)
                profits[i1], profits[i2] = profits[i2], profits[i1] # O(1)
                companies[i1], companies[i2] = companies[i2], companies[i1] # O(1)
    return companies[-3:] # O(1)

print(best_three1(company_profit))
print(best_three2(company_profit))
print(best_three3(company_profit))

