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
from random import randint

class Companies:
    def __init__(self):
        self.elems = []

    def print_elems(self):
        print(self.elems)

    def add_company(self, name, profit):
        self.elems.append((name,profit))

    def get_companies_max_profit(self): # O(n log n)
        self.elems.sort(key = lambda x: x[1], reverse=True) # O(n log n)
        quantity_company = 0 # O(1)
        result_lst = [] # O(1)
        for el in self.elems: # O(N)
            result_lst.append(el) #O(1)
            quantity_company += 1 # O(1)
            if quantity_company == 3: # O(1)
                break # O(1)

        return result_lst # O(1)

class Companies_2:
    def __init__(self):
        self.elems = {}

    def print_elems(self):
        print(self.elems)

    def add_company(self, name, profit):
        self.elems[name] = profit

    def get_companies_max_profit(self): # O(N)
        result_lst = [('',0),('',0),('',0)] # O(1)
        names_processed = [] # O(1)
        for i in range(3): # O(1)
            for name, profit in self.elems.items(): # O(N)
                if name in names_processed: # O(1)
                    continue
                if profit > result_lst[i][1]: # O(1)
                    result_lst[i] = (name,profit) # O(1)

            names_processed.append(result_lst[i][0]) # O(1)
        return result_lst # O(1)


if __name__ == '__main__':

    companies_obj = Companies()
    for i in range(10):
        companies_obj.add_company(f'name{i}',randint(0,100000))
    companies_obj.print_elems()
    print(companies_obj.get_companies_max_profit())

    companies_obj = Companies_2()
    for i in range(10):
        companies_obj.add_company(f'name{i}',randint(0,100000))
    companies_obj.print_elems()
    print(companies_obj.get_companies_max_profit())

"""
Выводы
сложность первого алгоритма O(n log n), сложность второго алгоритма # O(N).
Соответственно второй алгоритм предпочтительнее, так как имеет меньшую (линейную) сложность и на больших выборках
будет работать существенно быстрее первого.

"""

