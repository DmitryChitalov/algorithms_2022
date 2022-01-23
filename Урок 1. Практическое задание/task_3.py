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


def top3_1(companies): # O(N)
    top = []
    for key, value in companies.items(): 
        if len(top) == 0:
            top.append([key, value])
        elif len(top) == 1:
            if value > top[0][1]:
                top.append(top[0])
                top[0] = [key, value]
            else:
                top.append(value)
        elif len(top) == 2:
            if value > top[0][1]:
                top.append([1])
                top[1] = top[0]
                top[0] = [key, value]
            elif value > top[1][1]:
                top.append(top[1])
                top[1] = [key, value]
            else:
                top.append([key, value])
        else:
            if value > top[0][1]:
                top[2] = top[1]
                top[1] = top[0]
                top[0] = [key, value]
            elif value > top[1][1]:
                top[2] = top[1]
                top[1] = [key, value]
            elif value > top[2][1]:
                top[2] = [key, value]
    return top
            
def top3_2(companies): # O(nlogn)
    return sorted(companies.items(), 
                key=lambda companies: companies[1], reverse=True)[0:3]

    
companies = {
        'XP': 25_000_000,
        'Zomy': 27_000_000,
        'Besedka': 2_000_000,
        'Macrohard': 21_000_000,
        'Koyoka': 35_000_000,
        'EVM': 21_000_000,
        }
  

print(*top3_1(companies), sep = '\n')
print(*top3_2(companies), sep = '\n')
