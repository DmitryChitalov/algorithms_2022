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
from random import randrange


def data_dict_generator(n):
    data_dict = {}
    for i in range(n):
        name = ''.join([chr(randrange(65, 91)) for _ in range(5)])
        data_dict[name] = randrange(100, 1000)
    return data_dict


def max_profit1(data):  # Итоговая сложность решения O(n log n), так как сортировка
    data_1 = data.items()  # O(n)
    data_1 = sorted(data_1, key=lambda x: x[1])  # O(n log n)
    return data_1[-1], data_1[-2], data_1[-3]  # O(1)


def max_profit2(data):  # Итоговая сложность решения O(n)
    firm1, firm2, firm3 = '', '', ''  # O(1)
    for i in data:  # O(n)
        if firm1 == '' or data[i] >= data[firm1]:  # O(1)
            firm3 = firm2  # O(1)
            firm2 = firm1  # O(1)
            firm1 = i  # O(1)
        elif firm2 == '' or data[i] >= data[firm2]:  # O(1)
            firm3 = firm2  # O(1)
            firm2 = i  # O(1)
        elif firm3 == '' or data[i] >= data[firm3]:  # O(1)
            firm3 = i  # O(1)
    return (firm1, data[firm1]), (firm2, data[firm2]), (firm3, data[firm3])  # O(n)

"""
Функция max_profit2 более выгодная, потому что имеет меньшую сложность O(n) вместо O(n log n). 
С точки зрения использования памяти - тоже, потому что max_profit1 создает новый объект data_1,
сравнимый по размеру с исходным. А max_profit2 - только три лишние строки.
"""

firms_profit = data_dict_generator(100)
print(*max_profit1(firms_profit), sep='\n')
print('*********************************')
print(*max_profit2(firms_profit), sep='\n')
