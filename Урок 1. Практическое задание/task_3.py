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
from random import randint


def three_most_profit_companies_01(firms):  # Общая сложность O(N)
    firms_list = list(firms.items())  # O(N); создаем список кортежей
    for i in range(3):  # O(1)
        for j in range(i + 1, len(firms_list)):  # O(N);
            if firms_list[j][1] > firms_list[i][1]:  # O(1)
                firms_list[j], firms_list[i] = firms_list[i], firms_list[j]  # O(1)
    return dict(firms_list[0:3])  # O(1)


def three_most_profit_companies_02(firms):  # Общая сложность O(N log N)
    firms.sort(key=lambda val: val[1], reverse=True)  # O(N log N)
    return firms[0:3]  # O(1)


d_companies = {f'Firm_{randint(0, 30)}': randint(100, 10000) for i in range(randint(5, 20))}  # формируем словарь
l_companies = list(d_companies.items())  # формируем список из кортежей: ('орг-я', прибыль)
print(f'{len(d_companies)} {d_companies=}')
print(f'{three_most_profit_companies_01(d_companies)=}')
print(f'{three_most_profit_companies_02(l_companies)=}')

'''
Первый алгоритм со сложностью O(n) предпочтительнее O(N log N) при возрастающих размерах массивов
'''
