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


def max_cash_1(dict):
    """Функция принимает в аргумент словарь и возвращает 3 элементы с максимальными значениями
    Сложность: O(n log n)"""
    city_1 = sorted(dict.values())[-1]      # O(n log n)
    city_2 = sorted(dict.values())[-2]      # O(n log n)
    city_3 = sorted(dict.values())[-3]      # O(n log n)


    def get_key(value):
        """ Поиск ключей по значению в словаре, в аргумент принимает значение словаря
        Сложность: O(n)"""
        for k, v in dict.items():                                       # O(n)
            if v == value:                                              # O(n)
                return f'{k}:{v}'                                       # O(1)

    return f'{get_key(city_1)}\n{get_key(city_2)}\n{get_key(city_3)}'   # O(1)


# print(max_cash_1(city_cash))


def max_cash_2(dict):
    """Функция принимает в аргумент словарь и возвращает 3 элементы с максимальными значениями
    Сложность: O(n^2)"""
    listic_2 = list(dict.values())                          # O(len(n))

    def max_num(list):
        """Функция ищет максимальное значение в списке
        Сложность: O(n^2)"""
        listic = list[:]                                    # O(len(n))
        while len(listic) != 1:                             # O(1) + O(n)
            if listic[0] > listic[1]:                       # O(n) + O(1) + O(1)
                listic.insert(2, listic[0])                 # O(n) + O(1)
                listic.remove(listic[0])                    # O(n) + O(1)
            else:
                listic.remove(listic[0])                    # O(n) + O(1)
        return listic[0]                                    # O(1)

    lst = []                                                # O(1)
    while len(lst) < 3:                                     # O(n^2)
        max = max_num(listic_2)                             # O(n log n)
        for k, v in city_cash.items():
            if v == max:                                    # O(n)
                lst.append(f'{k}:{v}')                      # O(n)
                listic_2.remove(v)                          # O(n)
            else:
                continue                                    # O(1)

    return f'1 - {lst[0]}\n2 - {lst[1]}\n3 - {lst[2]}'      # O(1)




city_cash = {'Omsk': 65231, 'Moscow': 148547, 'kirov': 98564, 'Saratov': 101362, 'Kazan': 130754}


print(max_cash_2(city_cash))







